import os
from dotenv import load_dotenv
from pymongo import MongoClient
# from tabulate import tabulate

load_dotenv()
ATLAS_URI = os.getenv("ATLAS_URI")

client = MongoClient(ATLAS_URI)

try:
    print('--------------------------------------------')
    print("0. Successful connection")
    db = client["DemoDB"]  # database

    teachers = db["Teachers"]  # collection
    teachers.insert_many([
        {
            "name": "Anna Andersson",
            "department": "Mathematics",
            "courses": ["Algebra", "Calculus",
                        "Geometry"]
        },
        {
            "name": "Bertil Balder",
            "department": "Science",
            "courses": ["Physics", "Astronomy",
                        "Chemistry", "Biochemistry"]
        },
        {
            "name": "C Cederlöf",
            "department": "Computer Science",
            "courses": ["Programming 1", "Web Development",
                        "Python", "Databases 1", "Databases 2"]
        },
        {
            "name": "Donna Dunker",
            "department": "Social Studies",
            "courses": ["World History", "Civics",
                        "European History"]
        },
        {
            "name": "Erik Engels", "department": "Languages",
            "courses": ["English Literature", "English Grammar",
                        "Creative Writing", "Academic Writing",
                        "English Conversation"]
        },
    ])
    print('--------------------------------------------')
    print("1. Teacher, departments and courses added")

    students = db["Students"]  # collection
    students.insert_many([
        {
            "name": "Carl", "age": 32,
            "courses": [
                {"name": "Algebra", "grade": "C"},
                {"name": "Programming 1", "grade": "B"}
            ],
            "grade_history": [
                {"course": "Algebra", "grades": ["C", "B", "B"]},
                {"course": "Programming 1", "grades": ["B", "A"]}
            ]
        },
        {
            "name": "Max", "age": 27,
            "courses": [
                {"name": "World History", "grade": "A"},
                {"name": "Civics", "grade": "B"}
            ],
            "grade_history": [
                {"course": "World History", "grades": ["B", "A"]},
                {"course": "Civics", "grades": ["C", "B"]}
            ]
        },
        {
            "name": "Jenny", "age": 31,
            "courses": [
                {"name": "Algebra", "grade": "A"},
                {"name": "English Literature", "grade": "B"}
            ],
            "grade_history": [
                {"course": "Algebra", "grades": ["B", "A"]},
                {"course": "English Literature", "grades": ["B", "B", "A"]}
            ]
        },
        {
            "name": "Agnes", "age": 38,
            "courses": [
                {"name": "Chemistry", "grade": "F"},
                {"name": "Biochemistry", "grade": "F"}
             ],
            "grade_history": [
                {"course": "Chemistry", "grades": ["D", "F"]},
                {"course": "Biochemistry", "grades": ["F"]}
            ]
        },
        {
            "name": "Bertil", "age": 28,
            "courses": [
                {"name": "Geometry", "grade": "B"},
                {"name": "World History", "grade": "B"},
                {"name": "Programming 1", "grade": "A"}
             ],
            "grade_history": [
                {"course": "Geometry", "grades": ["C", "B"]},
                {"course": "World History", "grades": ["B", "B"]},
                {"course": "Programming 1", "grades": ["A"]}
            ]
        },
        {
            "name": "Dagny", "age": 31,
            "courses": [],
            "grade_history": [
                {"course": "Algebra", "grades": ["C"]}
            ]
        },
        {
            "name": "Erik", "age": 41,
            "courses": [
                {"name": "Physics", "grade": "A"},
                {"name": "Programming 1", "grade": "B"},
                {"name": "Astronomy", "grade": "A"}
            ],
            "grade_history": [
                {"course": "Physics", "grades": ["B", "A"]},
                {"course": "Programming 1", "grades": ["C", "B"]},
                {"course": "Astronomy", "grades": ["A"]}
            ]
        },
        {
            "name": "Fanny", "age": 21,
            "courses": [
                {"name": "Algebra", "grade": "A"},
                {"name": "English Grammar", "grade": "B"},
                {"name": "Chemistry", "grade": "A"}
            ],
            "grade_history": [
                {"course": "Algebra", "grades": ["B", "A"]},
                {"course": "English Grammar", "grades": ["B", "B"]},
                {"course": "Chemistry", "grades": ["A"]}
            ]
        },
    ])
    print('--------------------------------------------')
    print("2. Students, grades and history added")

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
    print('4. Find all teachers who teach a course where at least',
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

    print('--------------------------------------------')
    print('5. Add a new course to one of the students',
          '(e.g., "Programming", grade: "B") - ',
          'Make sure to update both courses and grade_history.')
    print('--------------------------------------------')
    students.update_one(
        {'name': 'Jenny'},
        {
            '$push': {
                'courses': {'name': 'Programming 1', 'grade': 'B'},
                'grade_history': {'course': 'Programming 1', 'grades': ['B']}
            }
        }
    )
    for student in students.find({"name": "Jenny"}):
        print(
            f"Name: {student.get('name', '')}, Age: {student.get('age', '')}"
        )
        if 'courses' in student:
            print('  Courses:')
            for course in student['courses']:
                print(
                    f"     {course.get('name', '')} -",
                    f"Grade: {course.get('grade', '')}"
                )
            print('   Grade history')
            for history in student.get('grade_history', []):
                grades_str = ", ".join(history.get('grades', []))
                print(f"    {history.get('course', '')} -",
                      f"Grades: {grades_str}")

    print('--------------------------------------------')
    print('6. Delete all students who are not enrolled in any course',
          '(i.e., courses array is empty or missing).')
    print('--------------------------------------------')
    
    students_to_delete = list(students.find({
            '$or': [
                {'courses': {'$exists': False}},
                {'courses': {'$size': 0}}
            ]
        }))

    if students_to_delete:
        for student in students_to_delete:
            print(
                f"Student by the name: {student.get('name', '')},",
                f"age: {student.get('age', '')}", end=' '
            )
            students.delete_one(student)
            print('does not have any courses and has been deleted')
    else:
        print('All students have courses')

    # print('--------------------------------------------')
    # print("""Bonus 1. Create a report that shows: course name,
    #       enrolled students, and average grade""")
    # print('--------------------------------------------')
    # # convert_grade = {'A': 5, 'B': 4, 'C': 3, 'D': 2, 'E': 1, 'F': 0}
    # # all_courses = {}
    # # course_data = []
    # # report_headers = ['Course', 'Number of students', 'Average grade']
    # # for student in students.find({}):
    # #     for course in student.get('courses', []):
    # #         course_name = course.get('name')
    # #         grade = course.get('grade')
    # #         if grade in convert_grade:
    # #             if course_name not in all_courses:
    # #                 all_courses[course_name] = {'count': 0, 'grades': []}
    # #             all_courses[course_name]['count'] += 1
    # #             all_courses[course_name]['grades'].append(
    # #                 convert_grade[grade]
    # #             )
    # # print('REPORT:')
    # # for course, stats in all_courses.items():
    # #     avg = 0
    # #     if stats['count']:
    # #         avg = round(sum(stats['grades'])/stats['count'], 2)
    # #     course_data.append([course, stats['count'], avg])
    # # print(tabulate(course_data, report_headers))
    # pipeline = [
    #     {'$unwind': '$courses'},
    #     {
    #         '$group': {
    #             '_id': '$courses.name',
    #             'students_count': {'$sum': 1},
    #             'grades': {'$push': '$courses.grade'}
    #         }
    #     },
    #     {
    #         '$project': {
    #             'course': '$_id',
    #             'student_count': 1,
    #             'avg_grade': {
    #                 '$avg': {
    #                     '$map': {
    #                         'input': '$grades',
    #                         'as': 'g',
    #                         'in': {
    #                             '$switch': {
    #                                 'branches': [
    #                                 ]
    #                             }
    #                         }
    #                     }
    #                 }
    #             }
    #         }
    #     }
    # ]

    # print('--------------------------------------------')
    # print("""Bonus 2. List each teacher with the number of unique students
    # enrolled in their courses.
    # Tips:
    # - Use $elemMatch, $unwind, $group, $lookup, and $match where needed.
    # - You may use grade conversion inside your pipeline using $switch or
    #   $map.
    # """)
    # print('--------------------------------------------')

    # # for teacher in teachers.find():
    # #     print(teacher['name'])
    # #     student_names = []
    # #     for course in teacher['courses']:
    # #         print(course)
    # #         for student in students.find(
    # #              {'courses': {'$elemMatch': {'name': course}}}
    # #         ):
    # #             if student['name'] not in student_names:
    # #                 student_names.append(student['name'])
    # #     print(teacher['name'], len(student_names))

    # pipeline = [
    #     {
    #         "$unwind": "$courses"  # 'flatten' courses from teachers
    # collection
    #     },
    #     {
    #         "$lookup": {  # search for
    #             "from": "Students",  # target: students collection
    #             "let": {"course_name": "$courses"},
    #             # create alias course_name from teachers courses
    #             "pipeline": [
    #                 {"$unwind": "$courses"},  # flatten student courses
    #                 {
    #                     "$match": {  # filter documents
    #                         "$expr": {  # evaluate expression
    #                             "$eq": [  # compare student/teachers courses
    #                                 "$courses.name",
    #                                 "$$course_name"
    #                             ]
    #                         }
    #                     }
    #                 },
    #                 {"$group": {"_id": "$name"}}  # group by student names
    #             ],
    #             "as": "students_in_course"
    #             # new array for students in the course
    #         }
    #     },
    #     {
    #         "$unwind": "$students_in_course"
    #         # flatten the new array (teacher/course/student)
    #     },
    #     {
    #         "$group": {
    #             "_id": "$name",  # group by teachers name
    #             "unique_students": {"$addToSet": "$students_in_course._id"}
    #             # add unique student names to a set
    #         }
    #     },
    #     {
    #         "$project": {
    #             "teacher": "$_id",  # output teachers name
    #             "student_count": {"$size": "$unique_students"},
    #             # output nbr of unique students
    #             "_id": 0  # hide MongoDBs default _id field
    #         }
    #     }
    # ]
    # results = list(teachers.aggregate(pipeline))
    # print(tabulate(
    #     [[r['teacher'], r['student_count']] for r in results],
    #     headers=["Teacher", "Number of unique students"]
    # ))

    # print('--------------------------------------------')
except Exception as e:
    print(e)
finally:
    client.close()
