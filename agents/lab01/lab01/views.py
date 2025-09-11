import os
from django.shortcuts import render
from dotenv import load_dotenv
# from openai import OpenAI
# from google import genai
from groq import Groq

load_dotenv()


def home(request):
    answer = None
    question = None
    if request.method == "POST":
        question = request.POST.get("question")
        '''Open AI'''
        # openai_api_key = os.getenv('OPENAI_API_KEY')
        # openai_client = OpenAI(api_key=openai_api_key)
        # try:
        #     response = openai_client.chat.completions.create(
        #         model="gpt-4o-mini",
        #         messages=[{"role": "user", "content": question}]
        #     )
        #     answer = response.choices[0].message.content
        # except Exception as e:
        #     answer = f"Error: {e}"
        
        '''Google'''
        # GEMINI_API_KEY = os.getenv('GOOGLE_API_KEY')
        # google_client = genai.Client()
        # try:
        #     response = google_client.models.generate_content(
        #         model='gemini-2.5-flash', contents=question)
        #     answer = response.text
        # except Exception as e:
        #     answer = f"Error: {e}"

        '''Groq'''
        groq_api_key = os.getenv('GROQ_API_KEY')
        groq_client = Groq(api_key=groq_api_key)
        try:
            response = groq_client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": question}]
            )
            answer = response.choices[0].message.content
        except Exception as e:
            answer = f"Error: {e}"

    return render(request, "home.html", {
        "answer": answer,
        "question": question
        })
