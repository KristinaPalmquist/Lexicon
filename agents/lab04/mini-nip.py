from transformers import pipeline
# , AutoTokenizer, AutoModelForSeq2SeqLM
import csv
import os
os.environ["TOKENIZERS_PARALLELISM"] = "false"  # or "true"

print("\n--- TASK 1 ---\n")

print("\n--- 1. INSTRUCTION REWRITE (FLAN-T5-base) ---\n")
instruction = pipeline("text2text-generation", model="google/flan-t5-base")

# input_text = input("Enter one sentence in English:\n")
input_text = (
    "She passes through a large mirror into another world and finds that, "
    "just as in a reflection, things there are reversed, including logic."
)

# prompt = f"Simplify this sentence: {input_text}"
prompt = (
    f"Rewrite a simpler version in English (exactly one sentence, "
    f"8-24 words, ending with period) of this sentence: {input_text}"
)

print("Response:", instruction(
    prompt,
    max_new_tokens=32,
    num_beams=5,
    no_repeat_ngram_size=3,
    do_sample=False
)[0]["generated_text"])

print("\n--- 2. SENTIMENT (DistilBERT SST-2) ---\n")

# sentence1 = input("Enter sentence number 1\n")
# sentence2 = input("Enter sentence number 2\n")
# sentence3 = input("Enter sentence number 3\n")
# examples = [sentence1, sentence2, sentence3]
examples = [
        "I hated the book and all the people portraid in it.",
        "This is a book that anyone can place on a shelf.",
        "Critical opinion of the book has generally been favourable."
]

sentiment = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
    )

for text in examples:
    result = sentiment(text)[0]
    print(
        f"Text: {text}\n"
        f"-> Label: {result['label']}, Score: {result['score']:.3f}\n"
    )

print("""
There is no neutral in this model because of the dataset it was
trained on. It makes a BINARY CLASSIFICATION. This forces the model to
return a sentiment even if the sentence is neutral.""")


print("\n--- TASK 2 ---\n")

print("\n--- B. ONE-SENTENCE SUMMARIZATION (DistilBART CNN) ---\n")

inputs = []

with open("lines.txt", 'r') as file:
    for line in file:
        line = line.strip()
        if line:
            inputs.append(line)

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

results = []
beams_rows = 0
beams_passed = 0
beams_tokens_out = 0
sampling_rows = 0
sampling_passed = 0
sampling_tokens_out = 0

for text in inputs:
    input_tokens = len(text.split())
    max_length = min(32, input_tokens)
    min_length = min(5, max_length)
    constraint_limit = 32
    
    try:
        beam_result = summarizer(
            text,
            max_length=max_length,
            min_length=min_length,
            num_beams=5,
            no_repeat_ngram_size=3,
            do_sample=False
        )[0]["summary_text"]
        beams_rows += 1
        beam_tokens = len(beam_result.split())
        beams_tokens_out += beam_tokens
        beam_constraint = beam_tokens <= constraint_limit
        if beam_constraint:
            beams_passed += 1
        beam_notes = ""
    except Exception as e:
        beam_result = ""
        beam_tokens = 0
        beam_constraint = False
        beam_notes = str(e)

    results.append([
        text,
        beam_result,
        "beam",
        beam_tokens,
        beam_constraint,
        beam_notes
    ])
    
    try:
        sampling_result = summarizer(
            text,
            max_length=max_length,
            min_length=min_length,
            do_sample=True,
            top_p=0.95,
            temperature=1.0
        )[0]["summary_text"]
        sampling_rows += 1
        sampling_tokens = len(sampling_result.split())
        sampling_tokens_out += sampling_tokens
        sampling_constraint = sampling_tokens <= constraint_limit
        if sampling_constraint:
            sampling_passed += 1
        sampling_notes = ""
    except Exception as e:
        sampling_result = ""
        sampling_tokens = 0
        sampling_constraint = False
        sampling_notes = str(e)

    results.append([
        text,
        sampling_result,
        "sampling",
        sampling_tokens,
        sampling_constraint,
        sampling_notes
    ])

with open("results.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow([
        "input",
        "output",
        "decoding",
        "tokens_out",
        "constraint_passed",
        "notes"
    ])
    writer.writerows(results)

print("\nBEAM")
print(f"Passed constraint: {round(beams_passed/beams_rows*100, 2)}%")
print(f"Average tokens out: {round(beams_tokens_out/beams_rows, 2)}")

print("\nSAMPLING")
print(f"Passed constraint: {round(sampling_passed/sampling_rows*100, 2)}%")
print(f"Average tokens out: {round(sampling_tokens_out/sampling_rows, 2)}")
