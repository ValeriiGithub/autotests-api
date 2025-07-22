import json

json_data = '{"name": "Иван", "age": 30, "is_student": false}'
parsed_data = json.loads(json_data)

print(parsed_data, type(parsed_data))

json_data = '{"name": "Иван", "age": 30, "is_student": false, "courses": ["Python", "QA Automation", "API Testing"], "address": {"city": "Москва", "zip": "101000"}}'
parsed_data = json.loads(json_data)

print(parsed_data, type(parsed_data))
print(parsed_data["courses"])
print(parsed_data["courses"][0])

data_user = {'name': 'Мария', 'age': 25, 'is_student': True}

json_string = json.dumps(data_user, indent=4)

print(json_string, type(json_string))

data_json_2 = '{"name": "\u041c\u0430\u0440\u0438\u044f", "age": 25, "is_student": true}'

parsed_data = json.loads(data_json_2)

print(parsed_data)


with open("json_examle.json", "r", encoding="utf-8") as file:
    data = json.load(file)
    print(data, type(data))

with open("json_user.json", "w", encoding="utf-8") as file:
    json.dump(data_user, file, indent=4, ensure_ascii=False)