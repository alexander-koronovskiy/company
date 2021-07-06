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

# read
with open("sum_file.csv") as config:
    for row in [line.split() for line in config]:
        files.append(dict(zip(columns, row)))

# check hash sum
for file in files:
    status = "NOT FOUND"
    content = ""
    try:
        with open(file["name"]) as f:
            content += f.read()
            if file["algorithm"] in hashlib.algorithms_available:
                if int(hashlib.sha1(content.encode("utf-8")).hexdigest(), 16) == int(
                    file["hash_sum"], 16
                ):
                    status = "OK"
                else:
                    status = "FAIL"
            else:
                status = "FAIL"
            print(file["name"], status)
    except FileNotFoundError:
        print(file["name"], status)
