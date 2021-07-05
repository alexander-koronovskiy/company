# -*- coding: cp1251 -*-
"""
Дан файл, содержащий имена файлов,
алгоритм хэширования (один из MD5/SHA1/SHA256) и соответствующие им хэш-суммы,
вычисленные по соответствующему алгоритму и указанные в файле через пробел.
Напишите программу, читающую данный файл и проверяющую целостность файлов.
"""
import hashlib

columns = ["name", "algorithm", "hash_sum"]
files = []

# считать названия файлов, алгоритмов, хэш суммы
with open("sum_file.csv") as config:
    for row in [line.split() for line in config]:
        files.append(dict(zip(columns, row)))

# по названию файла найти, проверить хэш, вывести итог
for file in files:
    status = "NOT FOUND"
    content = ""
    try:
        with open(file["name"]) as f:
            content += f.read()  # file buffer
            if int(hashlib.sha1(content.encode("utf-8")).hexdigest(), 16) == int(file["hash_sum"], 16):
                status = "OK"
            else:
                status = "FAIL"
            print(file["name"], status)
    except FileNotFoundError:
        print(file["name"], status)

# токенайзер для методов hashlib
