from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

# # Collection
# db = client["Library"]
# books = db["Books"]

# books.insert_many([
#     {"title": "Lexicon", "author": "Carl"},
#     {"title": "Star Wars", "author": "George Lucas"}
# ])

# Collection
db = client["School"]
students = db["Students"]

students.insert_many([
    {"name": "Emma", "age": 22, "courses": [
        {"name": "Math", "grade": "A"},
        {"name": "Programming", "grade": "B"},
        ]},
    {"name": "Haithem", "age": 27, "courses": [
        {"name": "Math", "grade": "C"},
        {"name": "Programming", "grade": "B"},
        ]},
])

for student in students.find():
    print(student)
