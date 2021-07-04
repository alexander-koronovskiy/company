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
    status = "NOT FOUND"
    try:
        with open(file["name"]) as f:
            f.readlines()
            print(file["hash_sum"])
    except FileNotFoundError:
        print(file["name"], status)

# ���������� ��� ������� �������� ��� �����
# ��������� ��������
