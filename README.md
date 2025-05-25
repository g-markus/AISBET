# AISBET - AI-Generation of Scenario-Based Exam Tasks

This repository contains the source code used in the paper "AI-Generation of Scenario-Based Exam Tasks".

The code creates training tasks for "Abschlusspruefung Fachinformatiker Anwendungsentwicklung Teil 2, Algorithmen, Pseudocode".


## Running the code.

The code runs as it is.

The examples are created with gemini-api. You need to provide an api-key in your .env.

Run googleAI.py for creation. The costs are about 2000 input tokens and 500 output tokens.

## Creation process

The creation is done by "few-shot-prompting", providing 5 examples of old examns.

Output goes to root directory "generated_exercise_*timestamp*.md"

The prompt used for generation is logged to prompt_to_generate_*timestamp*.md"

my_script.log holds debug messages of last execution.

## Description of files

```plaintext
root
|-output_and_logs holds the generaded excercises and log files (prompts used)
|
|-samples
| |-DE_....txt German example exams
| |-EN_....txt Example exams translated to english
| |-Example_x.txt Examples finally used for creation
| |-first_answer.txt output of very first try
| |-p1.txt Prompt used for very first try (examples excluded)
| |-prompt_no_examples_1.txt first evolution of prompt
| |-prompt_no_examples_2.txt second evolution of prompt
| |-prompt_no_examples_3.txt third, actual used evolution of prompt
| |-my_script.log log of last run with debug messages
| |-pdf_erl holds original pdf of example examns not provided here
|
|-source
| |-googleAI-x3.py test of generating 3 exercises at one shot, test no longer used
| |-googleAI.py main
```

