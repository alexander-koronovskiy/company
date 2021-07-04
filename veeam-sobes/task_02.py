# -*- coding: cp1251 -*-
"""
��� ����, ���������� ����� ������,
�������� ����������� (���� �� MD5/SHA1/SHA256) � ��������������� �� ���-�����,
����������� �� ���������������� ��������� � ��������� � ����� ����� ������.
�������� ���������, �������� ������ ���� � ����������� ����������� ������.
"""
import pandas as pd

names = ["name", "algorithm", "hash_sum"]

# ������� �������� ������, ����������, ��� �����
with open("sum_file.csv") as file:
    data = pd.DataFrame([line.split() for line in file])
    files_info = list(zip(data[0], data[1], data[2]))
print(dict(zip(names, files_info[0])))
