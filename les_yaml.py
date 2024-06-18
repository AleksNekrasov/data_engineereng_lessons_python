# pip install pyyaml  - установим через терминал yaml
import yaml

#----------------------------------------------------------------------------------------------------------
# write = 'w' - запись в файл
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

with open(r'connections.yaml', 'w') as file:  # создаем, если не было такого файла connections  и  записываем в него
    write_f = yaml.dump(l_connections, file)

#---------------------------------------------------------------------------------------------------------------
# read - 'r' - чтение из файла

with open(r'connections.yaml', 'r') as file:
    read_file = yaml.load(file, Loader=yaml.FullLoader)

print(read_file)
print(type(read_file))

