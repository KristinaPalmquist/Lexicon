import os
from dotenv import load_dotenv
from pymongo import MongoClient
# from collections import defaultdict

load_dotenv()
ATLAS_URI = os.getenv("ATLAS_URI")

client = MongoClient(ATLAS_URI)

try:
    print('--------------------------------------------')
    print("0. Successful connection")
    db = client["DemoDB"]  # database

    teachers = db["Teachers"]  # collection
    # teachers.insert_many([
    #     {
    #         "name": "Anna Andersson",
    #         "department": "Mathematics",
    #         "courses": ["Algebra", "Calculus",
    #                     "Geometry"]
    #     },
    #     {
    #         "name": "Bertil Balder",
    #         "department": "Science",
    #         "courses": ["Physics", "Astronomy",
    #                     "Chemistry", "Biochemistry"]
    #     },
    #     {
    #         "name": "C Cederlöf", 
    #         "department": "Computer Science",
    #         "courses": ["Programming 1", "Web Development",
    #                     "Python", "Databases 1", "Databases 2"]
    #     },
    #     {
    #         "name": "Donna Dunker",
    #         "department": "Social Studies",
    #         "courses": ["World History", "Civics",
    #                     "European History"]
    #     },
    #     {
    #         "name": "Erik Engels", "department": "Languages",
    #         "courses": ["English Literature", "English Grammar",
    #                     "Creative Writing", "Academic Writing",
    #                     "English Conversation"]
    #     },
    # ])
    # print('--------------------------------------------')
    # print("1. Teacher, departments and courses added")

    students = db["Students"]  # collection
    # students.insert_many([
    #     {
    #         "name": "Carl", "age": 32,
    #         "courses": [
    #             {"name": "Algebra", "grade": "C"},
    #             {"name": "Programming 1", "grade": "B"}
    #         ],
    #         "grade_history": [
    #             {"course": "Algebra", "grades": ["C", "B", "B"]},
    #             {"course": "Programming 1", "grades": ["B", "A"]}
    #         ]
    #     },
    #     {
    #         "name": "Max", "age": 27,
    #         "courses": [
    #             {"name": "World History", "grade": "A"},
    #             {"name": "Civics", "grade": "B"}
    #         ],
    #         "grade_history": [
    #             {"course": "World History", "grades": ["B", "A"]},
    #             {"course": "Civics", "grades": ["C", "B"]}
    #         ]
    #     },
    #     {
    #         "name": "Jenny", "age": 31,
    #         "courses": [
    #             {"name": "Algebra", "grade": "A"},
    #             {"name": "English Literature", "grade": "B"}
    #         ],
    #         "grade_history": [
    #             {"course": "Algebra", "grades": ["B", "A"]},
    #             {"course": "English Literature", "grades": ["B", "B", "A"]}
    #         ]
    #     },
    #     {
    #         "name": "Agnes", "age": 38,
    #         "courses": [
    #             {"name": "Chemistry", "grade": "F"},
    #             {"name": "Biochemistry", "grade": "F"}
    #          ],
    #         "grade_history": [
    #             {"course": "Chemistry", "grades": ["D", "F"]},
    #             {"course": "Biochemistry", "grades": ["F"]}
    #         ]
    #     },
    #     {
    #         "name": "Bertil", "age": 28,
    #         "courses": [
    #             {"name": "Geometry", "grade": "B"},
    #             {"name": "World History", "grade": "B"},
    #             {"name": "Programming 1", "grade": "A"}
    #          ],
    #         "grade_history": [
    #             {"course": "Geometry", "grades": ["C", "B"]},
    #             {"course": "World History", "grades": ["B", "B"]},
    #             {"course": "Programming 1", "grades": ["A"]}
    #         ]
    #     },
    #     {
    #         "name": "Dagny", "age": 31,
    #         "courses": [],
    #         "grade_history": [
    #             {"course": "Algebra", "grades": ["C"]}
    #         ]
    #     },
    #     {
    #         "name": "Erik", "age": 41,
    #         "courses": [
    #             {"name": "Physics", "grade": "A"},
    #             {"name": "Programming 1", "grade": "B"},
    #             {"name": "Astronomy", "grade": "A"}
    #         ],
    #         "grade_history": [
    #             {"course": "Physics", "grades": ["B", "A"]},
    #             {"course": "Programming 1", "grades": ["C", "B"]},
    #             {"course": "Astronomy", "grades": ["A"]}
    #         ]
    #     },
    #     {
    #         "name": "Fanny", "age": 21,
    #         "courses": [
    #             {"name": "Algebra", "grade": "A"},
    #             {"name": "English Grammar", "grade": "B"},
    #             {"name": "Chemistry", "grade": "A"}
    #         ],
    #         "grade_history": [
    #             {"course": "Algebra", "grades": ["B", "A"]},
    #             {"course": "English Grammar", "grades": ["B", "B"]},
    #             {"course": "Chemistry", "grades": ["A"]}
    #         ]
    #     },
    # ])
    # print('--------------------------------------------')
    # print("2. Students, grades and history added")





# Bonus Challenge - Aggregation Mastery
# These tasks will require you to use aggregation pipelines.
# 1. Create a report that shows:
# - Each course name
# - How many students are enrolled in that course
# - The average grade for that course
# (Tip: Convert grades to numbers, e.g., A = 5, B = 4, C = 3...)
# 2. List each teacher with the number of unique students
# enrolled in their courses.
# Tips:
# - Use $elemMatch, $unwind, $group, $lookup, and $match where needed.
# - You may use grade conversion inside your pipeline using $switch or $map.
# Don't forget that MongoDB works best when you think document-first,
# not SQL-style.

    print('--------------------------------------------')
    print('3. Find all students who have taken the course "Physics"',
          'and received an "A" (in either courses or grade_history).')
    print('--------------------------------------------')
    for student in students.find(
        {
            'courses': {'$elemMatch': {'name': 'Physics', 'grade': 'A'}},
            'grade_history': {
                '$elemMatch': {
                    'course': 'Physics',
                    'grades': 'A'
                }
            }
        },
        {'name': 1, 'age': 1}
    ):
        print(
            (
                f"Name: {student.get('name', '')}, "
                f"Age: {student.get('age', '')}"
            )
        )

    print('--------------------------------------------')
    print('4. Find all teachers who teach a course where at least ',
          'one student has an "A".')
    print('--------------------------------------------')
    for teacher in teachers.find():
        for course in teacher.get('courses', []):
            if students.find_one(
                {'courses': {'$elemMatch': {'name': course, 'grade': 'A'}}}
            ):
                print(
                    f"Name: {teacher.get('name', '')}, "
                    f"Department: {teacher.get('department', '')}"
                )
                break

    # print('--------------------------------------------')
    # print('5. Add a new course to one of the students ',
    #       '(e.g., "Programming", grade: "B") - ',
    #       'Make sure to update both courses and grade_history.')
    # print('--------------------------------------------')
    # students.update_one(
    #     {'name': 'Jenny'},
    #     {
    #         '$push': {
    #             'courses': {'name': 'Programming 1', 'grade': 'B'},
    #             'grade_history': {'course': 'Programming 1', 'grades': ['B']}
    #         }
    #     }
    # )
    # for student in students.find({"name": "Jenny"}):
    #     print(
    #         f"Name: {student.get('name', '')}, Age: {student.get('age', '')}"
    #     )
    #     if 'courses' in student:
    #         print('  Courses:')
    #         for course in student['courses']:
    #             print(
    #                 f"     {course.get('name', '')} -",
    #                 f"Grade: {course.get('grade', '')}"
    #             )
    #         print('   Grade history')
    #         for history in student.get('grade_history', []):
    #             grades_str = ", ".join(history.get('grades', []))
    #             print(f"    {history.get('course', '')} -",
    #                   f"Grades: {grades_str}")

    print('--------------------------------------------')
    print('6. Delete all students who are not enrolled in any course',
          '(i.e., courses array is empty or missing).')
    print('--------------------------------------------')

    try:
        for student in students.find({
            '$or': [
                {'courses': {'$exists': False}},
                {'courses': {'$size': 0}}
            ]
        }):
            print(
                f"Name: {student.get('name', '')}, ",
                f"Age: {student.get('age', '')} "
            )
            print('Hej')
            students.delete_one({student})
            print('does not have any courses and has been deleted')
    except Exception:
        print('All students have courses')
        
    # print('--------------------------------------------')
    # print('6. Update Carls course to Physics')
    # print('--------------------------------------------')
    # students.update_one(
    #     {"name": "Carl"},
    #     {'$set': {'courses': [{"name": "Physics", "grade": "C"}]}}
    # )
    # for student in students.find({"name": "Carl"}):
    #     print(
    #         f"Name: {student.get('name', '')}, Age: {student.get('age', '')}"
    #     )
    #     if 'courses' in student:
    #         for course in student['courses']:
    #             print(
    #                 f"  Course: {course.get('name', '')}, "
    #                 f"Grade: {course.get('grade', '')}"
    #             )
    # print('--------------------------------------------')
    # print('7. Delete Jenny')
    # print('--------------------------------------------')
    # students.delete_one({"name": "Jenny"})
    # jenny = students.find_one({"name": "Jenny"})
    # if jenny is None:
    #     print('Jenny not found in Students')
    # else:
    #     print(
    #         f"Name: {jenny.get('name', '')}, Age: {jenny.get('age', '')}"
    #     )
    #     if 'courses' in jenny:
    #         for course in jenny['courses']:
    #             print(
    #                 f"  Course: {course.get('name', '')}, "
    #                 f"Grade: {course.get('grade', '')}"
    #             )
    # print('--------------------------------------------')
    # print('Bonus 1. List students by course')
    # print('--------------------------------------------')
    # course_students = defaultdict(list)

    # for student in students.find():
    #     for course in student.get('courses', []):
    #         course_students[course.get('name', '')].append(
    #             student.get('name', '')
    #         )
    # for course_name, student_names in course_students.items():
    #     print(f'Course: {course_name}')
    #     for name in student_names:
    #         print(f'   Student: {name}')
    # print('--------------------------------------------')
    # print('Bonus 2. Count students in course')
    # print('--------------------------------------------')
    # count = students.count_documents({'courses.0': {'$exists': True}})
    # print(f"Number of students in at least 1 course: {count}")
    # print('--------------------------------------------')
except Exception as e:
    print(e)
finally:
    client.close()
