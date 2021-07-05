# -*- coding: cp1251 -*-
"""
��� ����, ���������� ����� ������,
�������� ����������� (���� �� MD5/SHA1/SHA256) � ��������������� �� ���-�����,
����������� �� ���������������� ��������� � ��������� � ����� ����� ������.
�������� ���������, �������� ������ ���� � ����������� ����������� ������.
"""
import hashlib

columns = ["name", "algorithm", "hash_sum"]
files = []

# ������� �������� ������, ����������, ��� �����
with open("sum_file.csv") as config:
    for row in [line.split() for line in config]:
        files.append(dict(zip(columns, row)))

# �� �������� ����� �����, ��������� ���, ������� ����
for file in files:
    status = "NOT FOUND"
    content = ""
    try:
        with open(file["name"]) as f:
            content += f.read()  # ����� ��������� ��� ����� �������� ��������
            print(
                file["name"],
                int(hashlib.sha224(content.encode("utf-8")).hexdigest(), 16)
                == int(file["hash_sum"], 16),
            )
    except FileNotFoundError:
        print(file["name"], status)

# ���������� ��� ������� hashlib
