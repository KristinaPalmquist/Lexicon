# vocabulary sheet 

# ————— Core concepts —————
# - **Model**: a trained neural network that maps input text to output text
#   labels.
# - **Weights / checkpoint**: the large files with the model’s learned
#   parameters.
# - **Inference** vs **training**: using a model to predict vs. updating its
#   weights with data.

# ————— Tokenization —————
# - **Tokenizer**: converts text ↔ tokens (integers). Loaded with   
#   `AutoTokenizer`.
# - **Token / Token ID**: a subword unit represented as an integer (what the
#   model actually reads).
# - **Vocabulary**: the set of all tokens a tokenizer knows.
# - **WordPiece**: tokenizer family used by BERT/DistilBERT (often uncased;
#   adds special tokens).
# - **SentencePiece**: tokenizer family used by T5/FLAN & Marian/OPUS-MT
#   (language-agnostic subwords).
# - **Detokenize**: convert token IDs back into human-readable text 
#   (optionally hiding special tokens).

# ————— Special tokens you’ll see —————
# - **[CLS]**: “classification” token at the start for BERT-style models 
#   (pooled summary for classifiers).
# - **[SEP]**: “separator/end” token at the end (and between paired sentences) 
#   for BERT-style models.
# - **</s> (EOS)**: end-of-sequence token used by T5/FLAN to signal “stop 
#   generating”.
# - **<pad>**: padding token used to equalize sequence lengths inside a batch.
# - **Pad token id**: the integer ID representing `<pad>` (e.g., 0 for many T5/
#   FLAN models).

# ————— Tensors & shapes —————
# - **Shape [B, L]**: tensors print as `torch.Size([batch_size, 
#   sequence_length])`.
# - **Batch size (B)**: how many sequences we process at once.
# - **Sequence length (L)**: number of **tokens** after tokenization (not 
#   characters/words).
# - **attention_mask**: `[B, L]` tensor with 1=real token, 0=padding; tells 
#   the model to ignore pads.
# - **Padding**: add `<pad>` tokens so all sequences in a batch share the same 
#   length.
# - **Truncation**: cut inputs longer than a chosen `max_length` (protects CPU 
#   time/memory).

# ————— Pipelines & Auto classes —————
# - **Pipeline**: a prebuilt function (e.g., `pipeline("summarization")`)
#   bundling tokenizer+model+decoding.
# - **Auto classes**: factory loaders that pick correct components, e.g.:
#   `AutoTokenizer.from_pretrained("google/flan-t5-base")`,
#   `AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-base")`.

# ————— Model families we use —————
# - **FLAN-T5 (encoder–decoder / seq2seq)**: instruction-tuned T5 (great for
#   text-to-text tasks).
# - **DistilBERT (encoder-only)**: lightweight BERT for classification
#   (expects [CLS]…[SEP]).
# - **DistilBART-CNN (encoder–decoder)**: distilled BART fine-tuned for news
#   summarization.
# - **OPUS-MT / Marian (encoder–decoder)**: translation models (e.g., EN→SV),
#   SentencePiece-based.
# - **Distillation**: compressing a large “teacher” into a smaller, faster
#   "student” model.

# ————— Generation (decoding) —————
# - **`.generate(...)`**: turns input token IDs into new output token IDs.
# - **Greedy**: always pick the top next token (deterministic, safe).
# - **Beam search (`num_beams`)**: explore several high-probability paths;
#   often more fluent; can repeat.
# - **Sampling (`do_sample=True`)**: add randomness; tune with **temperature**
#  and **top_p** for creativity.
# - **`max_new_tokens`**: cap on how many **generated** tokens to produce.
# - **`no_repeat_ngram_size`**: discourages repeating short phrases (reduces
#   loops/copypasta).
# - **`length_penalty`**: bias beams toward shorter/longer outputs.
# - **`skip_special_tokens=True`**: hide special tokens when decoding to text.

# ————— Performance & timing —————
# - **`time.perf_counter()`**: high-resolution wall-clock timer for quick
#   benchmarks.
# - **Latency vs throughput**: time per call vs items per second (batching
#   improves throughput).
# - **Warm-up / caches**: first call is slower; later calls are faster
#   (weights loaded, kernels warmed).
# - **Scaling with L²**: attention cost grows roughly with the square of
#   sequence length—keep prompts short on CPU.


#   ---------------------------------------------
#   Part 5 - Tokenizer
#   ---------------------------------------------


from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch


# text = "Transformers make local demos easy. Python is great for teaching."

# #   FLAN-T5-base tokenizer (SentencePiece):
# tok_flan = AutoTokenizer.from_pretrained("google/flan-t5-base")
# ids_flan = tok_flan.encode(text)
# print("\n--- TOKENS: FLAN-T5-base (SentencePiece) ---")
# print("Token IDs:", ids_flan[:20], "...")  
# #   </s>=1 - last id, 
# print("Decoded:", tok_flan.decode(ids_flan))


# # DistilBERT WordPiece (tokenizer):
# tok_bert = AutoTokenizer.from_pretrained(
#     "distilbert-base-uncased-finetuned-sst-2-english"
# )
# #   [CLS]=101 -  start token, single pool summary for the whole input
# #   [SEP]=102 -  trailing separator, marks the end, separates if multiple
# ids_bert = tok_bert.encode(text)
# print("\n--- TOKENS: DistilBERT WordPiece (tokenizer) ---")
# print("Token IDs:", ids_bert[:20], "...")
# print("Decoded:", tok_bert.decode(ids_bert))


# #   ---------------------------------------------
# #   Part 6 - From pipeline to Auto Classes
# #   ---------------------------------------------

# device = torch.device("cpu")
# model_id = "google/flan-t5-base"

# tok = AutoTokenizer.from_pretrained(model_id)

# model = AutoModelForSeq2SeqLM.from_pretrained(model_id).to(device)

# prompt = (
#     "Rewrite the sentence in simpler English. "
#   "output one sentence, end with a "
#     "period.\n"
#     "Sentence: 'Transformers lets us try modern AI models locally "
#   "for teaching"
#     ".'\n"
#     "Output:"
# )

# #    Encode
# enc = tok(prompt, return_tensors='pt').to(device)

# #   Tokenize to PyTorch tensors. We get:
# #       * input_ids: the integer tokens the model will read.
# #       * attention_mask: 1 for real tokens, 0 for pending

# print("\n--- SHAPES (inputs) ---")  # [batch_size, sequence_length]
# print("input_ids: ", enc.input_ids.shape)   # torch.Size([B, L])
# print("attention_mask: ", enc.attention_mask.shape)

# #   Why do we care about L? Because Transformer compute/memory scales roughly 
# #   with L^2 
# #   (self-attention compares each token to every other)

# # Generate:

# with torch.no_grad():
#     out_ids = model.generate(
#         **enc,  # unpacks dict as ... arguments
#         max_new_tokens=32,
#         num_beams=5,
#         no_repeat_ngram_size=3,     # prevents...
#         do_sample=False     # deterministic code
#     )

# print("\n--- SHAPES (output) ---")
# print("outputs_ids: ", out_ids.shape)

# #   Decode:

# out_text = tok.decode(out_ids[0], skip_special_tokens=True)
# #   skip special token </s>

# print("\n--- MANUAL GENERATION (FLAN-T5) ---")
# print(out_text)


# #   Sum:

# #   tokenize -> generate -> decode
# #   [batch, seq_len]

#   -------------------------------
#   LESSON 05
#   -------------------------------


#   ---------------------------------------------
#   Part 7 - Batching, padding, truncation
#   ---------------------------------------------

#   (for T5, pad_token_id is 0)

#   Shape: [batch_size, sequence_length], same as input_ids
#   Values: 1 means 'this position is a *real* token', 0 means 'this is PAD'

#   Padding mask (0s)
#   casual mask -> .generate()

#   truncation (max_length = ??tokens)
#   transformers scale roughly with ....

# import torch
# from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# model_id = 'google/flan-t5-base'
# device = torch.device('cpu')
# tok = AutoTokenizer.from_pretrained(model_id)
# model = AutoModelForSeq2SeqLM.from_pretrained(model_id).to(device)

# sentences = [
#     "Show one sentence summary of why Python is used in education.",
#     "Summarize the benefit of running models locally on CPU for teaching.",
#     "Explain in one sentence what a tokenizer does",
# ]

# enc_batch = tok(
#     [f"Respond in one sentence: {s}" for s in sentences],
#     return_tensors="pt", 
#     padding=True,
#     truncation=True,
#     max_length=96
# ).to(device)

# print("\n--- BATCHING ---")
# print("input_id shape:", enc_batch.input_ids.shape)
# #   [B, L] - batch size and sequence length
# print("attention_mask shape:", enc_batch.attention_mask.shape)
# print("pad token id:", tok.pad_token_id)

# #   torch.Size([3,20])
# #   in t5 pad token is usually 0

# with torch.no_grad():
#     out_batch = model.generate(
#         **enc_batch,   # unpacks input_ids and attention_mask
#         max_new_tokens=32,
#         num_beams=4,
#         do_sample=False  # no randomness
#     )


# print("\n--- BATCH OUTPUTS ---\n")
# for i, out in enumerate(out_batch):
#     print(f"{i+1}.", tok.decode(out, skip_special_tokens=True))


#   --------------------------------------------------------
#   Part 8 - Decoding strategies: greedy vs beam vs sampling
#   --------------------------------------------------------


model_id = 'google/flan-t5-base'
device = torch.device('cpu')
tok = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForSeq2SeqLM.from_pretrained(model_id).to(device)


def run_decode(prompt):
    enc = tok(prompt, return_tensors="pt").to(device)
    
    with torch.no_grad():
        # greedy decoding (high probability):
        g = model.generate(
            **enc,  # unpack
            max_new_tokens=64,
            do_sample=False,
            num_beams=1  # purely greedy
        )
        # beam search (several, keeps the best):
        b = model.generate(
            **enc,
            max_new_tokens=64,
            do_sample=False,
            num_beams=5     # small beam for CPU
        )
        #   sampling:
        s = model.generate(
            **enc,
            max_new_tokens=64,
            do_sample=True,  # enablestocastic, opposite of deterministic
            temperature=0.8,  # <1 = safer, >1 = more random
            top_p=0.9,   # nucleus sample, keep top 90 percent
            num_return_sequences=1
        )
    
        return (
            tok.decode(g[0], skip_special_tokens=True),
            tok.decode(b[0], skip_special_tokens=True),
            tok.decode(s[0], skip_special_tokens=True),
        )


cmp_prompt = (
    "Create one playful, single sentence analogy that explains how text is "
    "split for language models to understand. Do not use the words 'token' "
    "or 'tokenizer'. End with a period."
)

greedy_text, beam_text, sample_text = run_decode(cmp_prompt)

print("\n --- DECODE COMPARISON --- \n")
print("[Greedy]", greedy_text)  # safe
print("[Beam]", beam_text)  # structured (could copy)
print("[Sample]", sample_text)  # more variety


#  --- DECODE COMPARISON ---

# [Greedy] a tokenizer is a word that is used to describe a word that is used
# to describe a word. A tokenizer is a word that is used to describe a word
# that is used to describe a word. A tokenizer is a word that is used to
# describe a word
# [Beam] text is split for language models to understand. Do not use the words
# 'token' or 'tokenizer'. End with a period.
# [Sample] word = word + phrase.

#  --- DECODE COMPARISON ---

# [Greedy] The word 'token' is a syllable that means a word that is a token.
# [Beam] The word 'token' is used to describe a language model.
# [Sample] A typo in a word causes the word to look like a piece of paper.


#   --------------------------------------------------------
#   Part 9 - Timing (single prompt vs small batch on CPU)
#   --------------------------------------------------------

import time

model_id = 'google/flan-t5-base'
device = torch.device('cpu')
tok = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForSeq2SeqLM.from_pretrained(model_id).to(device)

sentences = [
    "Show one sentence summary of why Python is used in education.",
    "Summarize the benefit of running models locally on CPU for teaching.",
    "Explain in one sentence what a tokenizer does",
]

batch_prompts = [f"Respond in one sentence: {s}" for s in sentences] * 2

#   Time: single input
t0 = time.perf_counter()
# _ = conventional throw away variable name, we only care about the time here
_ = model.generate(
    **tok("Respond in one sentence: What is a tokenizer?",
          return_tensors="pt").to(device),
    max_new_tokens=24,
)

t1 = time.perf_counter()
# returns the float value of time in seconds,
# measures a short duration with highest available resolution

#   Time: small batch
enc2 = tok(
    batch_prompts,
    return_tensors="pt",
    padding=True,
    truncation=True,
    max_length=96
).to(device)

_ = model.generate(
    **enc2,
    max_new_tokens=24,
)

t2 = time.perf_counter()    # t2 - t1, end to end latency


print(f"Single input: approx. {(t1-t0):-3f}s")
print(f"Small batch: approx. {(t2-t1):-3f}s")
