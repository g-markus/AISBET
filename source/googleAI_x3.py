from dotenv import load_dotenv
import os
import random # Kept for example shuffling
import google.generativeai as genai
import datetime

# --- Load API Key ---
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")
if not API_KEY:
    print("Error: GOOGLE_API_KEY not found in environment variables or .env file.")
    exit()

# --- Configure SDK ---
try:
    genai.configure(api_key=API_KEY)
except Exception as e:
    print(f"Error configuring Google AI SDK: {e}")
    exit()

# --- Prepare Prompt (Includes simplified example loading/shuffling) ---
prompt = ""
try:
    sample_dir = 'samples'
    prompt_template_path = os.path.join(sample_dir, 'prompt_no_examples_2.txt')
    with open(prompt_template_path, encoding='utf-8') as prompt_file:
        prompt_text_template = prompt_file.read()

    examples_content = []
    for i in range(1, 6): # Load examples 1-5 if they exist
        example_path = os.path.join(sample_dir, f'Example_{i}.txt')
        if os.path.exists(example_path):
            try:
                with open(example_path, encoding='utf-8') as ex_file:
                    examples_content.append(ex_file.read())
            except Exception as e:
                 print(f"Warning: Error loading example {example_path}: {e}") # Minimal warning

    if examples_content:
        random.shuffle(examples_content)
        all_examples = "\n\n".join(examples_content)
    else:
        all_examples = ""

    prompt = prompt_text_template.replace('[EXAMPLES]', all_examples)

except FileNotFoundError:
    print(f"Error: Prompt template file not found at '{prompt_template_path}'.")
    exit()
except Exception as e:
    print(f"Error preparing prompt: {e}")
    exit()

if not prompt:
    print("Error: Prompt construction failed.")
    exit()

# --- Model and Generation Config ---
model_name = "gemini-1.5-pro-latest" # Or "gemini-1.5-flash-latest"
generation_config = genai.types.GenerationConfig(
    candidate_count=3,       # Request 3 candidates
    temperature=1.0,
    max_output_tokens=4096
)

# --- Instantiate Model ---
try:
    model = genai.GenerativeModel(
        model_name=model_name,
        generation_config=generation_config # Pass the config
    )
except Exception as e:
    print(f"Error instantiating model '{model_name}': {e}")
    exit()

# --- Timestamp and Save Prompt (Once) ---
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
prompt_filename = f"prompt_used_{timestamp}.md"
try:
    with open(prompt_filename, 'w', encoding='utf-8') as f:
        f.write(prompt)
    print(f"Prompt saved to: {prompt_filename}")
except IOError as e:
    print(f"Warning: Failed to save prompt file '{prompt_filename}': {e}")

# --- Generate Content and Save Candidates ---
print(f"Sending prompt to {model_name}, requesting 3 candidates...")
saved_count = 0
try:
    response = model.generate_content(prompt)

    if response.candidates:
        print(f"Received {len(response.candidates)} candidate(s). Saving...")
        for i, candidate in enumerate(response.candidates):
            candidate_num = i + 1
            output_filename = f"generated_exercise_{timestamp}_candidate_{candidate_num}.md"
            try:
                # Basic check for content parts before accessing text
                if candidate.content and candidate.content.parts:
                    generated_text = candidate.content.parts[0].text.strip()
                    with open(output_filename, 'w', encoding='utf-8') as f:
                        f.write(generated_text)
                    print(f"  - Saved candidate {candidate_num} to: {output_filename}")
                    saved_count += 1
                else:
                    # Handle cases where a specific candidate might be blocked/empty
                    finish_reason = getattr(candidate, 'finish_reason', 'UNKNOWN')
                    safety_ratings = getattr(candidate, 'safety_ratings', 'N/A')
                    print(f"  - Candidate {candidate_num} has no content. Skipped. Finish Reason: {finish_reason}, Safety: {safety_ratings}")

            except AttributeError:
                 print(f"  - Error accessing text for candidate {candidate_num}. Structure unexpected. Skipped.")
            except IndexError:
                 print(f"  - Error: No text part found for candidate {candidate_num}. Skipped.")
            except IOError as e:
                 print(f"  - Error saving candidate {candidate_num} to '{output_filename}': {e}")
            except Exception as e: # Catch other unexpected errors per candidate
                 print(f"  - Unexpected error processing candidate {candidate_num}: {e}")

    else:
        # Handle case where the entire response has no candidates (e.g., prompt blocked)
        print("\n--- API Response Error ---")
        print("The response contained no candidates.")
        try:
            print("Prompt Feedback:", response.prompt_feedback)
        except Exception:
            print("Could not retrieve prompt feedback.")

except Exception as e:
    print(f"\n--- Major API Call Error ---")
    print(f"An error occurred during the API call or processing: {e}")

# --- Final Summary ---
print(f"\n--- Script finished. Successfully saved {saved_count} answers. ---")