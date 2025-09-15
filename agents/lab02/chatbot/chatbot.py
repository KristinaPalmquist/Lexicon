from openai import OpenAI
import gradio as gr


messages = [{
    "role": "system",
    "content": "You are a helpful and kind API assistant."
},]


def chatbot(input):
    if input:
        messages.append({"role": "user", "content": input})
        # chat = openai.ChatCompletion.create(
        #     model="llama3.2",
        #     messages=messages
        # )
        ollama = OpenAI(
            base_url="http://localhost:11434/v1",
            api_key='ollama'
        )  # API key doesn't matter
        model_name = "llama3.2"
        chat = ollama.chat.completions.create(
            model=model_name, 
            messages=messages
        )
        reply = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        return reply


inputs = gr.Textbox(lines=7, label="Chat with AI")
outputs = gr.Textbox(lines=21, label="Reply")

gr.Interface(
    fn=chatbot,
    inputs=inputs,
    outputs=outputs,
    title="AI chatbot",
    description="Ask anything you want",
    theme="compact"
).launch(share=True)
