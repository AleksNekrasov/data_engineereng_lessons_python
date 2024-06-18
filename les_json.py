import json

dictionary = {
    "name": " sat",
    "rolno": 56,
    "cgpa": 8.4,
    "phonenumber": "89991223345"
}

# серилизация к json - приведение к объекту json
json_object = json.dumps(dictionary, indent=4)         # тут создаем json - объект indent=4 - форматирование для красоты и удобства. можно и без него
print(type(json_object))

# write - 'w' - запись : запишем в файл .json
with open("sample.json", 'w') as outfile:
    outfile.write(json_object)                          # тут json -объект записываем в файл

# то же самое, но не создавая json объект, а записывая сразу словарь dictionary
#with open("sample.json", "w") as outfile:
#    json.dump(dictionary, outfile)

# read - "r"  запись из файла в объект
with open("sample.json","r") as infile:
    new_json_object = json.load(infile)

print(new_json_object)
print(type(new_json_object))
