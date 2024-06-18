import pandas as pd

l_connections = [
    {
        "user": "first",
        "password": "345",
        "host": "127.0.0.1"
    },
    {
        "user": "second",
        "password": "346",
        "host": "127.0.0.1"
    }
]


df1 = pd.DataFrame(l_connections)
print(type(df1))
print(df1)

df1.to_csv("from_pandas.csv", index=False)   # записали в файл

# записать в переменную из файла
df2 = pd.read_csv("from_pandas.csv")

print(type(df2))
print(df2)
