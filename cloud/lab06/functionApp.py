import requests
import json

with open("testdata.json") as f:
    data = json.load(f)
    
print(f"📤 Sending {len(data)} student records to Azure Function...")

response = requests.post("http://localhost:7071/api/httppost",
                         headers={"Content-Type": "application/json"},
                         json=data)

print(f"✅ Status: {response.status_code}")

if response.status_code == 200:
    response_data = response.json()
    print(f"📄 {response_data['message']}")
    print("\n📋 Students processed:")
    for student in response_data['students']:
        print(f"  • {student['name']}: {student['grade']}")
else:
    print(f"❌ Error: {response.text}")