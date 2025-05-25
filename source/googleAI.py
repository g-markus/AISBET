from dotenv import load_dotenv
import os
import random

load_dotenv()

# Access the API key
API_KEY = os.getenv("GOOGLE_API_KEY")

import google.generativeai as genai
import datetime
import logging
import os # Added os for potential environment variable usage


# --- Ensure logging is configured to show DEBUG messages ---
# Add this basic configuration if you haven't configured logging elsewhere
# Adjust filename, level, and format as needed for your application
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='my_script.log',
    filemode='a'
)
# ----------------------------------------------------------



# --- Configuration ---

# 1. Configure the Google AI SDK with your API Key
try:
    if not API_KEY or API_KEY == "YOUR_GOOGLE_AI_API_KEY":
         raise ValueError("API Key not set. Please replace 'YOUR_GOOGLE_AI_API_KEY' or set the GOOGLE_API_KEY environment variable.")
    genai.configure(api_key=API_KEY)
except ValueError as e:
    print(f"Configuration Error: {e}")
    exit() # Exit if API key is not configured
except Exception as e:
    print(f"An unexpected error occurred during configuration: {e}")
    exit()


# --- Prepare Model and Generation Config ---
generation_config = genai.types.GenerationConfig(
    temperature=0.7,         # Recommended starting point
    max_output_tokens=4096   # Generous limit for a full exercise
    #candidate_count=3
    # top_p=0.9,             # Alternative to temperature, usually leave unset if temp is set
    # top_k=40,              # Usually leave unset
    # stop_sequences=["--END--"] # Example, if needed
)


# 2. Load Prompt and Examples (Ensure files are in the correct path relative to the script)

# Using os.path.join for better path handling might be safer
sample_dir = 'samples' # Assuming 'samples' is a subdirectory
with open(os.path.join(sample_dir, 'prompt_no_examples_3.txt'), encoding='utf-8') as prompt_file:
    prompt_text = prompt_file.read()


sample_dir = 'samples' # Assuming 'samples' is a subdirectory
examples_data = [] # Store dictionaries: {'id': filename, 'content': text}

logging.debug("Loading examples...") # Use logging instead of print for consistency
for i in range(1, 6): # Assuming you want examples 1 through 5
    example_filename = f'Example_{i}.txt'
    example_path = os.path.join(sample_dir, example_filename)

    if os.path.exists(example_path):
         try:
             with open(example_path, encoding='utf-8') as ex_file:
                 content = ex_file.read()
                 # Store both an identifier and the content
                 examples_data.append({'id': example_filename, 'content': content})
                 logging.debug(f"  - Loaded: {example_path}")
         except Exception as e:
              # Log actual errors with error level
              logging.error(f"  - Error loading {example_path}: {e}")
    else:
         # Log warnings for non-critical issues like missing files
         logging.warning(f"  - Example file not found: {example_path}")

# --- Shuffle the loaded examples data ---
if examples_data: # Only shuffle if examples were actually loaded
    logging.debug(f"Loaded {len(examples_data)} examples successfully. Shuffling their order...")
    random.shuffle(examples_data) # Shuffles the list of dictionaries in-place
    logging.debug("Examples shuffled.")

    # --- Log the new order using the identifiers ---
    shuffled_order_ids = [item['id'] for item in examples_data]
    logging.debug(f"Shuffled example order: {shuffled_order_ids}")
    # --------------------------------------------

    # --- Extract and join the content in the shuffled order ---
    shuffled_content = [item['content'] for item in examples_data]
    all_examples = "\n\n".join(shuffled_content)
    # -------------------------------------------------------

else:
    logging.warning("No examples were loaded. Cannot shuffle or join.")
    all_examples = "" # Assign empty string if no examples

prompt = prompt_text.replace('[EXAMPLES]', all_examples)

# 3. Choose the Model
#    Select an appropriate Google AI model (e.g., "gemini-1.5-pro-latest", "gemini-1.5-flash-latest")
#    Check https://ai.google.dev/models/gemini for available models
model_name = "gemini-1.5-pro-latest" # Using the latest Pro model

# 4. Define Output Filename
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
output_filename = f"generated_exercise_{timestamp}.md"
prompt_filename = f"prompt_to_generate_{timestamp}.md"


# Instantiate the generative model
try:
    model = genai.GenerativeModel(
        model_name=model_name,
        # generation_config=generation_config, # Uncomment to use
        # safety_settings=safety_settings      # Uncomment to use
        )
except Exception as e:
    print(f"Error instantiating model '{model_name}': {e}")
    exit()

# --- Make the API Call ---
try:
    print(f"Sending prompt to Google AI API using model: {model_name}...")

    # Generate content using the simpler API for single-turn text generation
    response = model.generate_content(prompt)

    # --- Process Response and Save to File ---

    # Check for safety blocks or other reasons for no content
    if not response.parts:
        print("\n--- API Response Error ---")
        print("The response was empty. This might be due to safety filters.")
        try:
            print("Prompt Feedback:", response.prompt_feedback)
        except Exception:
            print("Could not retrieve prompt feedback.")
        # Consider printing the full response object for debugging if needed
        # print("Full Response object:", response)

    # Check if response text exists (it should if response.parts is not empty)
    elif hasattr(response, 'text'):
        generated_content = response.text.strip()

        print("API call successful. Attempting to save response...")

        try:
            # Save the generated content
            with open(output_filename, 'w', encoding='utf-8') as f:
                f.write(generated_content)

            # Save the prompt used
            with open(prompt_filename, 'w', encoding='utf-8') as f:
                f.write(prompt)

            print(f"\n--- Success ---")
            print(f"Generated exercise successfully saved to: {output_filename}")
            print(f"Prompt used saved to: {prompt_filename}")

        except IOError as e:
            print(f"\n--- File Writing Error ---")
            print(f"Failed to write generated content to file '{output_filename}': {e}")
            print("\n--- Generated Content (Not Saved) ---")
            print(generated_content)

    else:
        # Handle unexpected response structure
        print("\n--- API Response Error ---")
        print("Could not parse expected 'text' attribute from the Google AI API response.")
        print("Full Response object:", response)

# --- Error Handling for API Call ---
except Exception as e:   
    print(f"An error occurred during the API call or processing: {e}")
   