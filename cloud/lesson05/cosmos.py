from pymongo import MongoClient
import os
from dotenv import load_dotenv

### CONFIGURE ###
load_dotenv()
connection_string = os.getenv('CONNECTION_STRING')
database_name = 'student_db'
collection_name = 'students'


### CONNECT ###
try:
    client = MongoClient(connection_string)
    client.admin.command('ismaster')
    print('✅ Successfully connected to Azure Cosmos DB / MongoDB!')
    
except Exception as e:
    print(f'❌ Connection failed: {e}')
    exit()

print('-'*60)


### CREATE ###
database = client[database_name]
collection = database[collection_name]

student_records = [
    {'name': 'Agneta Andersson', 'grade': 92},
    {'name': 'Bob Bernhardz', 'grade': 78},
    {'name': 'Cilla Ceder', 'grade': 85},
    {'name': 'Dan Danielsson', 'grade': 95},
    {'name': 'Ebba Engels', 'grade': 75},
    {'name': 'Fredrik Fredriksson', 'grade': 68},
    {'name': 'Greta Gunnarsson', 'grade': 82},
    {'name': 'Harry Hinder', 'grade': 73},
    {'name': 'Inga Ismael', 'grade': 94},
]

try:
    collection.insert_many(student_records)
    print(f'Added {len(student_records)} students to the database')
except Exception as e:
    print(f'Insertion failed {e}')
print('-'*60)


### CRUD ###
# Create
add_name = 'Jill Johnson'
add_grade = 88
print(f'STUDENT TO ADD: \n{add_name}, grade: {add_grade}')
collection.insert_one({'name': add_name, 'grade': add_grade})
print('-'*60)

# Read
query_filter = {'grade': {'$gt': 80}}
high_grade_students = collection.find(query_filter)
high_grade_count = collection.count_documents({'grade': {'$gt': 80}})
print(f'STUDENTS WITH GRADE > 80 ({high_grade_count} STUDENTS):')
for student in high_grade_students:
    print(f"{student['name']}, {student['grade']}")
print('-'*60)

# Update
update_name = 'Ebba Engels'
update_grade = 79
print(f'STUDENT TO UPDATE: \n{update_name}, new grade: {update_grade}')
collection.update_one({'name': update_name}, {'$set': {'grade': update_grade}})
print('-'*60)

# Delete
delete_name = 'Agneta Andersson'
print(f'STUDENT TO DELETE: \n{delete_name}')
collection.delete_one({'name': delete_name})
print('-'*60)


student_count = collection.count_documents({})
print(f'COMPLETE LIST OF STUDENTS ({student_count} STUDENTS):')
for student in collection.find():
    print(f'{student['name']}, {student['grade']}')
print('-'*60)


### CLEAR ###
try:
    result = collection.delete_many({})
    print(f'✅ Successfully cleared {result.deleted_count} students from database!')
except Exception as e:
    print(f'❌ Clearing database failed: {e}')


### CLOSE ###
client.close()
print('Database connection closed!')
