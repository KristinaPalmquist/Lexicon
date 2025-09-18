#   Vocabulary

# - **Model**: a trained neural network that maps input text to output text or
#   labels.
# - **Weights / checkpoint**: the learned parameters of that model (the big
#   files we download).
# - **Tokenizer**: converts text → **tokens** (subwords/IDs) for the model,
#   and back again.
# - **Tokens**: pieces of text (not necessarily full words). Length limits and
#   speeds are
#   measured in tokens, so “max_new_tokens” is about subwords, not words.
# - **Transformer (architecture)**: the neural network design (self-attention
#   tc.) used
#   by most state-of-the-art language models.
# - **Transformers (library)**: the Hugging Face Python library we import to
#   use models.
# - **Pipeline**: a prebuilt function (e.g., `pipeline("sentiment-analysis")`)
#   that handles tokenizer + model + decoding for a common task.
# - **Inference** vs **training**:
#   * Inference = using a trained model to make predictions.
#   * Training/fine-tuning = updating weights with data.
# - **Encoder–decoder** vs **decoder-only**:
#   * Encoder–decoder (e.g., T5/BART): good for text-to-text tasks (summarize/
#   translate).
#   * Decoder-only (e.g., GPT-style): good for next-token text continuation.
# - **Deterministic decoding** (beam search, no sampling): stable, repeatable
#   outputs.
# - **Sampling** (temperature, top-p): more creative/varied but less
#   predictable.


# "How a pipeline call works (mental model):"
#   1) Your input text → **tokenizer** → token IDs.
#   2) Token IDs → **model** (forward pass on CPU) → output logits.
#   3) **Decoding** turns logits into text (beam search or sampling).
#   4) Output tokens → detokenize → final string.


#   Setup
#   Text-to-text generation
#   Sentiment analysis (classification)
#   Summarization - distile bart daily mail (?)
#   Translation - opus MT (?)

#   transformers
#   accelerate - tiny runtime helper


#   /opt/anaconda3/envs/condaML/bin/pip install


from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM
import os
os.environ["TOKENIZERS_PARALLELISM"] = "false"  # or "true"

#   ---------------------------------------------
#   Part 1 - Text Generation with FLAN-T5-base
#   ---------------------------------------------

gen = pipeline("text2text-generation", model="google/flan-t5-base")

prompt = (
    "Produce exactly ONE family-friendly joke. "
    "One sentence, 10-20 words, end with a period."
)

print("\n--- TEXT GENERATION (FLAN-T5-base, deterministic) ---\n")

print(gen(
    prompt,
    max_new_tokens=32,
    num_beams=5,
    no_repeat_ngram_size=3,
    do_sample=False
)[0]["generated_text"])


#   ---------------------------------------------
#   Part 2 - Sentiment Analysis (DistilBert model)
#   ---------------------------------------------

sentiment = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
    )

print("\n--- SENTIMENT ANALYSIS ---\n")

examples = [
    "I absolutely lova coding in Python!",
    "This is driving me crazy",
    "It's okay, not great, not terrible."
]

for text in examples:
    result = sentiment(text)[0]
    print(
        f"Text: {text}\n"
        f"- Label: {result['label']}, Score: {result['score']:.3f}\n"
    )


#   ---------------------------------------------
#   Part 3 - Summarization (DistilBART CNN)
#   ---------------------------------------------


# summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

print("\n--- SUMMARIZATION ---\n")

article = (
    """Python is a popular programming language known for readability and a
    rich ecosystem. Hugging Face Transformers lets developers run
    state-of-the-art AI models locally. With pipelines, tasks like text
    generation, sentiment analysis, and summarization become easy to
    prototype"""
)

summary = summarizer(
    article,
    max_length=20,  # subword pieces ... NOT words
    min_length=15,
    do_sample=False
)[0]["summary_text"]

print("Original: ", article)
print("\nSummary:", summary)


#   ---------------------------------------------
#   Part 4 - TRANSLATION (EN -> SV) (OPUS-MT)
#   ---------------------------------------------


# translator = pipeline(
#     "translation",
#     model="Helsinki-NLP/opus-mt-en-es"
# )

# english = "Transformers pipelines make it simple to try models locally."
# swedish = translator(english)[0]["translation_text"]


# print("EN:", english)
# print("SV:", swedish)


model_name = "google/flan-t5-base"

# This will automatically find and load the 'model.safetensors' file
tokenizer = AutoTokenizer.from_pretrained(model_name)

model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

input_text = "Transformer pipelines make it easy to try models locally."
input_lang = "English"
output_lang = "Swedish"
prompt_text = (
    f"Translate this {input_lang} sentence to {output_lang}: {input_text}"
)

encoded_input = tokenizer(prompt_text, return_tensors="pt")
output_tokens = model.generate(**encoded_input)
decoded_output = tokenizer.decode(output_tokens[0], skip_special_tokens=True)

print(prompt_text)
print(f"{input_lang} text: {input_text}")
print(f"{output_lang} text: {decoded_output}")


# ----- LESSON04 -----
