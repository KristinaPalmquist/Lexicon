from django.shortcuts import render, redirect
from dotenv import load_dotenv
import os
from openai import OpenAI
import google.generativeai as genai
from groq import Groq


load_dotenv()


def home(request):
    answer = None
    question = None
    language_model = None
    if request.method == "POST":
        question = request.POST.get("question")
        language_model = request.POST.get("language_model")
        answer = 'Don - the big bad AI machine'
        # request.session['answer'] = answer
        # request.session['question'] = question
        # return redirect('home')
        '''Open AI'''
        if language_model == 'openai':
            openai_api_key = os.getenv('OPENAI_API_KEY')
            openai_client = OpenAI(api_key=openai_api_key)
            try:
                response = openai_client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[{"role": "user", "content": question}]
                )
                answer = response.choices[0].message.content
                request.session['answer'] = answer
                request.session['question'] = question
                return redirect('home')
            except Exception as e:
                answer = f"Error: {e}"
        elif language_model == 'gemini':
            GEMINI_API_KEY = os.getenv('GOOGLE_API_KEY')
            google_client = genai.Client()
            try:
                response = google_client.models.generate_content(
                    model='gemini-2.5-flash', contents=question)
                answer = response.text
                request.session['answer'] = answer
                request.session['question'] = question
                return redirect('home')
            except Exception as e:
                answer = f"Error: {e}"
        else:
            groq_api_key = os.getenv('GROQ_API_KEY')
            groq_client = Groq(api_key=groq_api_key)
            try:
                response = groq_client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[{"role": "user", "content": question}]
                )
                answer = response.choices[0].message.content
                request.session['answer'] = answer
                request.session['question'] = question
                return redirect('home')
            except Exception as e:
                answer = f"Error: {e}"

    # Retrieve and clear from session after redirect
    if 'answer' in request.session:
        answer = request.session.pop('answer')
    if 'question' in request.session:
        question = request.session.pop('question')

    return render(request, "home.html", {
        "answer": answer,
        "question": question
        })
