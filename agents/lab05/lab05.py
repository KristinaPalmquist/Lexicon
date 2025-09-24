# Todays Lab - 2025-09-22

# Implement a small script that
# (1) batches inputs with padding/truncation,
# (2) generates outputs with three decoding strategies (greedy, beam,
# sampling),
# (3) runs simple automatic checks on the outputs, and (4) times
# single vs. small-batch runs — all locally on CPU.

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch
import math
import time

# Use this model & setup:
# - Model: google/flan-t5-base
model_id = 'google/flan-t5-base'
# - Run on CPU only.
device = torch.device('cpu')
tok = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForSeq2SeqLM.from_pretrained(model_id).to(device)
# - Tokenization must use padding=True, truncation=True, and your chosen
# max_length (justify by comment in code).
max_length = 96  # I used the same as Aladdin in lesson
# - For generation use the same max_new_tokens across all strategies so
# results are comparable.
max_new_tokens = 24


def run_decode(prompt):
    enc = tok(prompt, return_tensors="pt").to(device)
    with torch.no_grad():
        greedy_decode = model.generate(
            **enc,
            max_new_tokens=max_new_tokens,
            do_sample=False,
            num_beams=1
        )
        beam_decode = model.generate(
            **enc,
            max_new_tokens=max_new_tokens,
            do_sample=False,
            num_beams=5
        )
        sampling_decode = model.generate(
            **enc,
            max_new_tokens=max_new_tokens,
            do_sample=True,
            temperature=0.8,
            top_p=0.9,
            num_return_sequences=1
        )
        print("{:<10}{}".format(
            "[Greedy]", tok.decode(greedy_decode[0], skip_special_tokens=True)
        ))
        print("{:<10}{}".format(
            "[Beam]", tok.decode(beam_decode[0], skip_special_tokens=True)
        ))
        print("{:<10}{}".format(
            "[Sample]",
            tok.decode(sampling_decode[0], skip_special_tokens=True)
        ))

        return (
            tok.decode(greedy_decode[0], skip_special_tokens=True),
            tok.decode(beam_decode[0], skip_special_tokens=True),
            tok.decode(sampling_decode[0], skip_special_tokens=True),
        )


#  Write functions to check each generated line (no manual judging):


# 1. One sentence? (exactly one terminal punctuation among . ! ?)
def one_sentence(text):
    return int(sum(c in '.!?' for c in text) == 1)


# 2. Ends with a period?
def ends_with_period(text):
    return int(text.strip().endswith('.'))


# 3. Word count window (choose a window, e.g., 8–24 words)
def count_words(text):
    min_words = 8
    max_words = 24
    return int(min_words <= len(text.split()) <= max_words)


# 4. Repetition flag (detect repeated bigrams/trigrams or obvious loops)
def repetition_flag(text):
    words = text.lower().split()
    bigrams = [" ".join(words[i:i+2]) for i in range(len(words)-1)]
    trigrams = [" ".join(words[i:i+3]) for i in range(len(words)-2)]
    for seqs in [bigrams, trigrams]:
        counts = {}
        for seq in seqs:
            counts[seq] = counts.get(seq, 0) + 1
            if counts[seq] > 1:
                return 0
    return 1


prompts = [
    (
        "Rewrite the sentence in simpler English. End with a period. "
        "Sentence: 'Python’s clear syntax helps beginners focus on "
        "problem-solving.'"
    ),
    (
        "Rewrite the sentence in simpler English. End with a period. "
        "Sentence: 'Version control lets teams track changes and work "
        "safely together.'"
    ),
    (
        "Rewrite the sentence in simpler English. End with a period. "
        "Sentence: 'Preprocessing text often includes lowercasing and "
        "removing extra spaces.'"),
    (
        "Rewrite the sentence in simpler English. End with a period. "
        "Sentence: 'Short prompts run faster on CPU because attention "
        "scales with length.'"),
    (
        "Explain in one sentence what a learning rate does. "
        "End with a period."),
    (
        "Explain in one sentence what an API key is used for. "
        "End with a period."),
    (
        "Explain in one sentence what a unit test checks. "
        "End with a period."),
    (
        "Explain in one sentence what a tokenizer does in NLP. "
        "End with a period."),
    (
        "Summarize in one sentence: 'Pipelines bundle tokenization, the "
        "model, and decoding. They are great for quick demos on CPU.'"),
    (
        "Summarize in one sentence: 'Batching several prompts can improve "
        "throughput. Padding and masks keep shapes compatible.'"),
    (
        "Summarize in one sentence: 'Beam search is deterministic and "
        "often fluent. Sampling adds creativity but may drift.'"),
    (
        "Summarize in one sentence: 'SentencePiece and WordPiece split "
        "text into subwords. This keeps vocabulary small and improves "
        "coverage.'")
 ]

print("-"*60)
print("A) Batch tokenization (padding & truncation)")
print("-"*60)
# - Batch all 12 prompts (you may prepend a short instruction like Respond in
# one sentence: if you want).
batch_prompts = [
    f"Respond in one sentence, ending with a period {p}"
    for p in prompts
]

# - Tokenize with padding=True, truncation=True, and max_length you choose
# (briefly comment in code why).
enc = tok(
    batch_prompts,
    return_tensors="pt",
    padding=True,
    truncation=True,
    max_length=max_length
).to(device)

# - Print:
#  input_ids.shape and attention_mask.shape
print("input_ids:", enc.input_ids.shape)
print("attention_mask:", enc.attention_mask.shape)
#  The tokenizer’s pad token id
print("tokenizer's pad token id:", tok.pad_token_id)

#  (Optional) Print the last row of attention_mask to show
# 1s (real tokens) vs 0s (padding).
print("\nLast line of attention mask:")
print(enc.attention_mask[-1])

print("-"*60)
print("B) Decode the same batch three ways")
print("-"*60)
#  Run generation for the exact same tokenized batch with these strategies
# and print outputs for each prompt:

# - Greedy: do_sample=False, num_beams=1
# - Beam: do_sample=False, num_beams = 3 or 5 (pick one and note it in a
#   comment)
# - Sampling: do_sample=True with your chosen temperature (≈0.7–0.9) and
#   top_p (≈0.8–0.95)

# For each prompt, print three one-liners labeled [Greedy], [Beam], [Sample].
# Keep them on separate lines or in a simple table.

prompts_results = []
for i, prompt in enumerate(prompts):
    print(f"Prompt {i+1}:")
    greedy_output, beam_output, sample_output = run_decode(prompt)
    outputs = [{i: [greedy_output, beam_output, sample_output]}]
    prompt_result = {
        'greedy': {
            'output': greedy_output,
            'one_sentences': one_sentence(greedy_output),
            'ends_with_period': ends_with_period(greedy_output),
            'word_count': count_words(greedy_output),
            'repetition': repetition_flag(greedy_output),
        },
        'beam': {
            'output': beam_output,
            'one_sentences': one_sentence(beam_output),
            'ends_with_period': ends_with_period(beam_output),
            'word_count': count_words(beam_output),
            'repetition': repetition_flag(beam_output),
        },
        'sample': {
            'output': sample_output,
            'one_sentences': one_sentence(sample_output),
            'ends_with_period': ends_with_period(sample_output),
            'word_count': count_words(sample_output),
            'repetition': repetition_flag(sample_output),
        }
    }
    prompts_results.append({i: prompt_result})


print("-"*60)
print("C) Automatic checks (programmatic, no prose)")
print("-"*60)


headers = ["Check", "Greedy", "Beam", "Sample"]
checks = ["one_sentences", "ends_with_period", "word_count", "repetition"]

totals = {
    "greedy": {check: 0 for check in checks},
    "beam": {check: 0 for check in checks},
    "sample": {check: 0 for check in checks},
}

for result in prompts_results:
    prompt_result = list(result.values())[0]
    for strategy in ["greedy", "beam", "sample"]:
        for check in checks:
            totals[strategy][check] += prompt_result[strategy][check]

# - Constraint pass-rate = % that pass checks 1+2+3
pass_counts = {"greedy": 0, "beam": 0, "sample": 0}

for result in prompts_results:
    prompt_result = list(result.values())[0]
    for strategy in pass_counts:
        checks_passed = (
            prompt_result[strategy]["one_sentences"] == 1 and
            prompt_result[strategy]["ends_with_period"] == 1 and
            prompt_result[strategy]["word_count"] == 1
        )
        if checks_passed:
            pass_counts[strategy] += 1

print("\nConstraint Pass Rate (checks 1, 2 & 3):")
print("{:<10} {}".format(
        "STRATEGY",
        "PASSED"
    )
)
for strategy in pass_counts:
    print(
        "{:<10} {:.1f}%".format(
            "[" + strategy.capitalize() + "]",
            round(pass_counts[strategy] / len(prompts) * 100, 2)
        )
    )

# - Avg. word count (and optionally std dev)
awc_strategies = {
    "greedy": {
        'average_word_count': 0,
        'standard_deviation': 0,
        'word_counts': []
    },
    "beam": {
        'average_word_count': 0,
        'standard_deviation': 0,
        'word_counts': []
    },
    "sample": {
        'average_word_count': 0,
        'standard_deviation': 0,
        'word_counts': []
    }
}

for result in prompts_results:
    prompt_result = list(result.values())[0]
    for strategy in awc_strategies:
        output_text = prompt_result[strategy]
        output_text = prompt_result[strategy]['output']
        word_count = len(output_text.split())
        awc_strategies[strategy]['average_word_count'] += word_count
        awc_strategies[strategy]['word_counts'].append(word_count)

for strategy in awc_strategies:
    avg = awc_strategies[strategy]['average_word_count'] / len(prompts)
    awc_strategies[strategy]['average_word_count'] = avg
    wc_list = awc_strategies[strategy]['word_counts']
    std_dev = math.sqrt(sum((wc-avg)**2 for wc in wc_list) / len(prompts))
    awc_strategies[strategy]['standard_deviation'] = std_dev

print("\nAverage word count per strategy:")
print("{:<10} {:<12} {:<12}".format(
        "STRATEGY",
        "WORD COUNT",
        "STD DEV"
    )
)
for strategy in awc_strategies:
    print(
        "{:<10} {:<12.2f} {:<12.2f}".format(
            "[" + strategy.capitalize() + "]",
            awc_strategies[strategy]['average_word_count'],
            awc_strategies[strategy]['standard_deviation']
        )
    )

# - % with repetition (from check 4)
rep_strategies = {"greedy": 0, "beam": 0, "sample": 0}
for result in prompts_results:
    prompt_result = list(result.values())[0]
    for strategy in rep_strategies:
        if prompt_result[strategy]['repetition'] == 0:
            rep_strategies[strategy] += 1

print("\nPercentage with repetition per strategy:")
print("{:<10} {}".format(
        "STRATEGY",
        "REPETITION"
    )
)
for strategy in rep_strategies:
    print(
        "{:<10} {:.1f}%".format(
            "[" + strategy.capitalize() + "]",
            round(rep_strategies[strategy]/len(prompts), 2)*100
        )
    )

# Print a compact summary table to the console (one row per strategy).
print("\nSummary table - (Number of prompts that pass the test)")
table_headers = ['STRATEGY', 'ONE SENTENCE', 'ENDS WITH PERIOD', 'WORD COUNT',
                 'REPETITION']
strategies = ["greedy", "beam", "sample"]

print("{:<10} {:<14} {:<18} {:<12} {:<10}".format(*table_headers))
for strategy in strategies:
    print("{:<10} {:<14} {:<18} {:<12} {:<10}".format(
        "[" + strategy.capitalize() + "]",
        totals[strategy]["one_sentences"],
        totals[strategy]["ends_with_period"],
        totals[strategy]["word_count"],
        totals[strategy]["repetition"]
    ))


# (Optional) Add a simple on-topic keyword flag per prompt if you want;
# otherwise skip.
def contains_keyword(text, keyword):
    return int(keyword.lower() in text.lower())


keywords = [
    {'Python': 0},
    {'track': 0},
    {'preprocessing': 0},
    {'CPU': 0},
    {'learning': 0},
    {'API': 0},
    {'test': 0},
    {'NLP': 0},
    {'CPU': 0},
    {'padding': 0},
    {'deterministic': 0},
    {'subwords': 0},
    ]

for i, result in enumerate(prompts_results):
    key = list(keywords[i].keys())[0]
    found = 0
    for strategy in strategies:
        output_text = list(result.values())[0][strategy]['output']
        if contains_keyword(output_text, key):
            found += 1
    keywords[i][key] = found

print("\nKeywords found")
print("{:<7} {:<21} {}".format("PROMPT", 'KEYWORD', 'NUMBER FOUND'))
for i, key_dict in enumerate(keywords):
    print("{:<7} {:<21} {}".format(
        f"{i+1}.",
        list(key_dict.keys())[0],
        list(key_dict.values())[0]
        )
    )

print("-"*60)
print("D) Tiny timing")
print("-"*60)

#  Measure on CPU with time.perf_counter():
#  - Single input: tokenize → generate for 1 representative prompt
#   (use the same max_new_tokens).
t0 = time.perf_counter()

_ = model.generate(
    **tok(prompts[0],
          return_tensors="pt").to(device),
    max_new_tokens=max_new_tokens
)

#  - Small batch: tokenize → generate for a batch (use all 12 prompts,
#   or duplicate them once).
t1 = time.perf_counter()

enc2 = tok(
    batch_prompts,
    return_tensors="pt",
    padding=True,
    truncation=True,
    max_length=96
).to(device)

_ = model.generate(
    **enc2,
    max_new_tokens=max_new_tokens
)

t2 = time.perf_counter()
# Print two numbers (seconds, 3 decimals):
#  Single input: ~Xs
print(f"Single input: ~{(t1-t0):-3f}s")
#  Small batch : ~Ys
print(f"Small batch: ~{(t2-t1):-3f}s")
