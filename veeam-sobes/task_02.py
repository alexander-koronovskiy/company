# -*- coding: cp1251 -*-
"""
Дан файл, содержащий имена файлов,
алгоритм хэширования (один из MD5/SHA1/SHA256) и соответствующие им хэш-суммы,
вычисленные по соответствующему алгоритму и указанные в файле через пробел.
Напишите программу, читающую данный файл и проверяющую целостность файлов.
"""
import pandas as pd

names = ["name", "algorithm", "hash_sum"]

# считать названия файлов, алгоритмов, хэш суммы
with open("sum_file.csv") as file:
    data = pd.DataFrame([line.split() for line in file])
    files_info = list(zip(data[0], data[1], data[2]))
print(dict(zip(names, files_info[0])))
