import requests
import json
import sqlite3

connection = sqlite3.connect("BibliaDigital_db.sqlite")
cursor = connection.cursor()
# cursor.execute('''CREATE TABLE BibliaDigital_db''')
chapter = input("Please enter the chapter: ")
Key = "ebhS2NNjcH5S0FPRBLgL53fjGLsC6TIhBxLoiEhc"
Url = f"https://www.abibliadigital.com.br/api/verses/nvi/sl/{chapter}"


response = requests.get(Url)
print(response.status_code)
print(response.text)
print(response.headers)

plot = response.json()
with open("BibliaDigital.json", 'w') as BD:
    json.dump(plot, BD, indent=4)
print(json.loads(response.text))
print("მოცემული თავის  მოკლე შინაარსია: ", json.dumps(plot['verses'], indent=4))
for n in plot['verses']:
    print(n, plot["verses"])
