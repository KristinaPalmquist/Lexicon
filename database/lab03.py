import os
from dotenv import load_dotenv
from pymongo import MongoClient
from collections import defaultdict

load_dotenv()
ATLAS_URI = os.getenv("ATLAS_URI")
# link = "mongodb://localhost:27017/"

client = MongoClient(ATLAS_URI)

try:
    print('--------------------------------------------')
    print("1. Successful connection")
    print('--------------------------------------------')
    db = client["DemoDB"]  # database
    students = db["Students"]  # collection
    students.insert_many([
        {"name": "Carl", "age": 32, "courses": [
            {"name": "Math", "grade": "C"},
            {"name": "Programming", "grade": "B"},
            ]},
        {"name": "Max", "age": 27, "courses": [
            {"name": "Math", "grade": "A"},
            {"name": "History", "grade": "B"},
            ]},
        {"name": "Jenny", "age": 31, "courses": [
            {"name": "Math", "grade": "A"},
            {"name": "Programming", "grade": "B"},
            ]},
        {"name": "Agnes", "age": 38, "courses": [
            {"name": "Math", "grade": "F"},
            {"name": "Programming", "grade": "F"},
            ]},
        {"name": "Bertil", "age": 28, "courses": [
            {"name": "Math", "grade": "B"},
            {"name": "History", "grade": "B"},
            {"name": "Programming", "grade": "A"},
            ]},
        {"name": "Dagny", "age": 31, "courses": []},
        {"name": "Erik", "age": 41, "courses": [
            {"name": "Math", "grade": "A"},
            {"name": "Programming", "grade": "B"},
            {"name": "Physics", "grade": "A"},
            ]},
        {"name": "Fanny", "age": 21, "courses": [
            {"name": "Math", "grade": "A"},
            {"name": "Programming", "grade": "B"},
            {"name": "Physics", "grade": "A"},
            ]},
    ])
    print('--------------------------------------------')
    print('2. All students')
    print('--------------------------------------------')
    for student in students.find():
        print(
            (
                f"Name: {student.get('name', '')}, "
                f"Age: {student.get('age', '')}"
            )
        )
        if 'courses' in student:
            for course in student['courses']:
                print(
                    f"  Course: {course.get('name', '')}, "
                    f"Grade: {course.get('grade', '')}"
                )
    print('--------------------------------------------')
    print('3. Name = Jenny')
    print('--------------------------------------------')
    for student in students.find({"name": "Jenny"}):
        print(
            f"Name: {student.get('name', '')}, Age: {student.get('age', '')}"
        )
        if 'courses' in student:
            for course in student['courses']:
                print(
                    f"  Course: {course.get('name', '')}, "
                    f"Grade: {course.get('grade', '')}"
                )
    print('--------------------------------------------')
    print('4. Over 30')
    print('--------------------------------------------')
    for student in students.find({'age': {'$gt': 30}}):
        print(
            f"Name: {student.get('name', '')}, Age: {student.get('age', '')}"
        )
    print('--------------------------------------------')
    print('5. Add a course for Max')
    print('--------------------------------------------')
    students.update_one(
        {"name": "Max"},
        {'$push': {'courses': {"name": "Art", "grade": "F"}}}
    )
    for student in students.find({"name": "Max"}):
        print(
            f"Name: {student.get('name', '')}, Age: {student.get('age', '')}"
        )
        if 'courses' in student:
            for course in student['courses']:
                print(
                    f"  Course: {course.get('name', '')}, "
                    f"Grade: {course.get('grade', '')}"
                )
    print('--------------------------------------------')
    print('6. Update Carls course to Physics')
    print('--------------------------------------------')
    students.update_one(
        {"name": "Carl"},
        {'$set': {'courses': [{"name": "Physics", "grade": "C"}]}}
    )
    for student in students.find({"name": "Carl"}):
        print(
            f"Name: {student.get('name', '')}, Age: {student.get('age', '')}"
        )
        if 'courses' in student:
            for course in student['courses']:
                print(
                    f"  Course: {course.get('name', '')}, "
                    f"Grade: {course.get('grade', '')}"
                )
    print('--------------------------------------------')
    print('7. Delete Jenny')
    print('--------------------------------------------')
    students.delete_one({"name": "Jenny"})
    jenny = students.find_one({"name": "Jenny"})
    if jenny is None:
        print('Jenny not found in Students')
    else:
        print(
            f"Name: {jenny.get('name', '')}, Age: {jenny.get('age', '')}"
        )
        if 'courses' in jenny:
            for course in jenny['courses']:
                print(
                    f"  Course: {course.get('name', '')}, "
                    f"Grade: {course.get('grade', '')}"
                )
    print('--------------------------------------------')
    print('Bonus 1. List students by course')
    print('--------------------------------------------')
    course_students = defaultdict(list)

    for student in students.find():
        for course in student.get('courses', []):
            course_students[course.get('name', '')].append(
                student.get('name', '')
            )
    for course_name, student_names in course_students.items():
        print(f'Course: {course_name}')
        for name in student_names:
            print(f'   Student: {name}')
    print('--------------------------------------------')
    print('Bonus 2. Count students in course')
    print('--------------------------------------------')
    count = students.count_documents({'courses.0': {'$exists': True}})
    print(f"Number of students in at least 1 course: {count}")
    print('--------------------------------------------')
except Exception as e:
    print(e)
finally:
    client.close()
