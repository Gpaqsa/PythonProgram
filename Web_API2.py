# import requests
# import json
#
# city = 'Tbilisi'
# key = '6686275845d0da1e1964f820280542af'
# # url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric"
# # url = f"https://api.openweathermap.org/data/2.5/weather"
# payload = {'q': city, 'appid': key, 'units': 'metric'}
# resp = requests.get("https://api.openweathermap.org/data/2.5/weather", params=payload)
# # print(resp.headers)
# # print(type(resp.text))
# # print(type(resp.json()))
#
# res = resp.json()
# res = json.loads(resp.text)
# print(res)
# print(json.dumps(res, indent=4))

# POST Method
# get
# import requests
# payload = {'firstname': 'ANN', 'lastname': 'paksa'}
# ket = "6686275845d0da1e1964f820280542af"
# url = ""

# import json
# import requests
#
# city = input("Please enter the city:  ")
# Key = "6686275845d0da1e1964f820280542af"
# Url = f"Https://api.openweathermap.org/data/2.5/forecast/daily?q={city}&cnt={16}&appid={Key}"
# # payload = {'q': city, 'appid': Key, 'units': 'metric'}
# response = requests.get(Url)
# print(response.status_code)
# print(response.text)
# # respp = response.json()
# # print(json.dumps(respp, indent=4))
# # # print("Current temperature: ", respp['main']["temp"], 'C')




import requests
import json

city = input('please enter the city:')
key = 'c3f4a1234628a0e9f356eb5a43648a89'

url = f'https://api.openweathermap.org/data/2.5/weather?q={city}7D&appid={key}'
response = requests.get(url)
print(response)
response_in_json = response.json()
json_structured = json.dumps(response_in_json, indent=3)
print(json_structured)


