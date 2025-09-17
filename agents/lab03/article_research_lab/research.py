import os
import ollama

articles_path = 'agents/lab03/article_research_lab/articles'
summaries_path = 'agents/lab03/article_research_lab/summaries'

articles = os.listdir(articles_path)


def askAI(question):
    response = ollama.chat(model='llama3.2', messages=[
        {
            'role': 'user',
            'content': question
        },
    ])
    return response


def getSummary(content, article):
    question = (
        f"Summarize this text: {content} "
        "I only want the summary, no opening remarks or other comments."
    )
    response = askAI(question)
    save_path = os.path.join(summaries_path, article)
    with open(save_path, 'w') as file:
        file.write(response['message']['content'])


for article in articles:
    file_path = os.path.join(articles_path, article)
    if os.path.isfile(file_path):
        with open(file_path, 'r') as file:
            content = file.read()
            getSummary(content, article)

summaries_filenames = os.listdir(summaries_path)
summaries = []

for summary in summaries_filenames:
    file_path = os.path.join(summaries_path, summary)
    if os.path.isfile(file_path):
        with open(file_path, 'r') as file:
            content = file.read()
            summaries.append(content)

summaries_text = ""
for idx, summary in enumerate(summaries, 1):
    summaries_text += f"\n--- Summary {idx} ---\n{summary}\n"

question = (
    "Compare these articles. What are the common themes and key differences?\n"
    "Here are the summaries:\n"
    f"{summaries_text}"
)

response = askAI(question)
print(response['message']['content'])
