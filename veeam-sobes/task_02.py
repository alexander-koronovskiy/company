# -*- coding: cp1251 -*-
"""
��� ����, ���������� ����� ������,
�������� ����������� (���� �� MD5/SHA1/SHA256) � ��������������� �� ���-�����,
����������� �� ���������������� ��������� � ��������� � ����� ����� ������.
�������� ���������, �������� ������ ���� � ����������� ����������� ������.
"""
columns = ["name", "algorithm", "hash_sum"]
files = []

# ������� �������� ������, ����������, ��� �����
with open("sum_file.csv") as config:
    for row in [line.split() for line in config]:
        files.append(dict(zip(columns, row)))

# �� �������� ����� �����, ��������� ���, ������� ����
for file in files:
    print(file["name"])  # with open() as f: f.reads()
