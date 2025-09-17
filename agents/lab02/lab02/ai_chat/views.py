from django.shortcuts import render, redirect
from dotenv import load_dotenv
# import os
from openai import OpenAI
import Markdown

load_dotenv()


def home(request):
    answer = None
    question = None
    if request.method == "POST":
        question = request.POST.get("question")
        answer = 'No question has been asked yet'
        request.session['answer'] = answer
        request.session['question'] = question
        return redirect('home')
    ollama = OpenAI(
        base_url="http://localhost:11434/v1",
        api_key='ollama'
    )  # API key doesn't matter
    model_name = "llama3.2"
    response = ollama.chat.completions.create(model=model_name, messages=messages)
    answer = response.choices[0].message.content

    print(Markdown(answer))

    # Retrieve and clear from session after redirect
    if 'answer' in request.session:
        answer = request.session.pop('answer')
    if 'question' in request.session:
        question = request.session.pop('question')

    return render(request, "home.html", {
        "answer": answer,
        "question": question
        })
