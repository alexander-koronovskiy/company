# -*- coding: cp1251 -*-
"""
Реализовать программу, осуществляющую копирование файлов
в соответствии с конфигурационным файлом.
Конфигурационный файл должен иметь формат xml.
Для каждого файла в конфигурационном файле должно быть указано его имя,
исходный путь и путь, по которому файл требуется скопировать.
"""

import shutil
import xml.etree.ElementTree as ET


# парсинг xml файла, копирование
def copying(config, source_path, destination_path, file_name):
    root = ET.parse(config).getroot()
    for type_tag in root.findall("file"):
        src_path = type_tag.get(source_path)
        destination = type_tag.get(destination_path)
        f_name = type_tag.get(file_name)
        shutil.copy(src_path + "\\" + f_name, destination)


copying("config.xml", "source_path", "destination_path", "file_name")
