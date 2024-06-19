print("""1. Почитать про YAML формат: https://ru.wikipedia.org/wiki/YAML
2. Почитать про JSON формат: https://habr.com/ru/articles/554274/
3. Создать класс, в классе хранить лист словарей (как у меня в коде пример с подключениями - можете придумать что-нибудь своё, например в словарях данные людей будут или ещё что-нибудь)
4. Сделать 2 метода для работы с YAML - для сохранения в файл и для чтения из файла. Название фала должно передаваться в метод входным параметром.
5. Сделать 2 метода для работы с JSON - для сохранения в файл и для чтения из файла. Название фала должно передаваться в метод входным параметром.
6. В другом поле хранить Pandas DataFrame с данными. Написать ещё 2 метода - для сохранения данных в файл .csv и для чтения данных из .csv файла в датафрейм.
Так же написать для 4, 5, 6 пунктов методы, которые будут просто отображать данные, которые внутри объекта хранятся.
7. Попробовать при помощи объекта класса прочитать данные из YAML формата, а сохранить - в JSON.
8. Наоборот: прочитать данные из JSON, сохранить в YAML.""")
import yaml
import json
import pandas as pd


class Archive:
    __dict_lists = list()
    __dict_json = {'main': ""}
    __dict_panda = pd

    #===YAML======YAML======YAML======YAML======YAML======YAML======YAML======YAML======YAML======YAML======YAML======YAML===
    def write_yaml(self, file: str, lst: list) -> None:  # запись в файл
        with open(file, "w") as w_f:  # 'w'-write запись -перезапись , 'a'- append дозаписывание в файл
            yaml.dump(lst, w_f)  # что записываем, куда записываем

    def read_yaml(self, file: str) -> list:  # чтение из файла
        with open(file, "r") as r_f:
            read_file = yaml.load(r_f, Loader=yaml.FullLoader)
            return read_file

    def append_yaml(self, file: str, lst: list) -> None:
        with open(file, "a") as a_f:  # 'w'-write запись -перезапись , 'a'- append дозаписывание в файл
            yaml.dump(lst, a_f)  # что записываем, куда записываем

    #==JSON====JSON====JSON====JSON====JSON====JSON====JSON====JSON====JSON====JSON====JSON====JSON====JSON====JSON====JSON==
    def write_json(self, file: str, dct: dict) -> None:
        with open(file, "w") as w_f:  # 'w'-write запись -перезапись , 'a'- append дозаписывание в файл
            json.dump(dct, w_f, indent=4)  # что записываем, куда записываем

    def read_json(self, file: str) -> dict:
        with open(file, "r") as r_f:
            read_file = json.load(r_f)
            return read_file

    def append_json(self, file: str, dct: dict) -> None:
        # дозапись файла в значение словаря ПОКА НЕ ГОТОВА ЭТА ФУНКЦИЯ
        with open(file, "w") as a_f:
            json.dump(self.__dict_json, a_f)  # что записываем, куда записываем

    #**CSV****CSV****CSV****CSV****CSV****CSV****CSV****CSV****CSV****CSV****CSV****CSV****CSV****CSV****CSV****CSV**
    def write_csv(self, file: str, lst: list) -> None:
        self.__dict_panda = pd.DataFrame(lst)  # записали в переменную в формате панда
        self.__dict_panda.to_csv(file, index=False)  # записали в файл(file) без индекса

    def read_csv(self, file: str):
        self.__dict_panda = pd.read_csv(file)
        return self.__dict_panda


l_connections = [
    {
        "user": "first",
        "password": "345"
    },
    {
        "aser": "second",
        "password": "346",
        "host": "127.0.0.1"
    }
]

l_connections2 = [
    {
        "user": "two",
        "password": "34445",
        "host": "127.0.0.2"
    },
    {
        "user": "secondary",
        "password": "37746",
        "host": "127.0.0.1"
    }
]
#путь к файлу
file_path_yaml = "practic.yaml"
# инициализация класса
testClass = Archive()

# запись - перезапись в файл
testClass.write_yaml(file=file_path_yaml, lst=l_connections)
print("=+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print(testClass.read_yaml(file=file_path_yaml))
print(type(testClass.read_yaml(file_path_yaml)))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++=")

#дозапись в файл
testClass.append_yaml(file=file_path_yaml, lst=l_connections2)

print(testClass.read_yaml(file=file_path_yaml))
print("______________________________________________________________________________________________________")

print("==JSON==JSON==JSON==JSON==JSON==JSON==JSON==JSON==JSON==JSON==JSON==JSON==JSON==JSON==JSON==JSON==JSON")

file_path_json = "practic.json"

dictionary = {
    "name": " sat",
    "rolno": 56,
    "cgpa": 8.4,
    "phonenumber": "89991223345"
}

testClass.write_json(file=file_path_json, dct=dictionary)
#testClass.append_json(file=file_path_json, dct=dictionary)
#testClass.append_json(file=file_path_json, dct=dictionary)

print(testClass.read_json(file_path_json))
print(type(testClass.read_json(file_path_json)))

print("::CSV::::CSV::::CSV::::CSV::::CSV::::CSV::::CSV::::CSV::::CSV::::CSV::::CSV::::CSV::")

file_path_csv = "practic.csv"
testClass.write_csv(file=file_path_csv, lst=l_connections2)
print(testClass.read_csv(file=file_path_csv))

#testClass.write_yaml(file=file_path_yaml, lst=testClass.read_json(file=file_path_json)) # запись в Yaml файл из файля json
#testClass.write_json(file=file_path_json, dct=testClass.read_yaml(file=file_path_yaml)) # запись в json из yaml