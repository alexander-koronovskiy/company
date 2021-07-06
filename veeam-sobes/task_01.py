import shutil
import xml.etree.ElementTree as ET


# xml file parsing, copying
def copying(config, source_path, destination_path, file_name):
    root = ET.parse(config).getroot()
    for type_tag in root.findall("file"):
        src_path = type_tag.get(source_path)
        destination = type_tag.get(destination_path)
        f_name = type_tag.get(file_name)
        shutil.copy(src_path + "\\" + f_name, destination)


copying("config.xml", "source_path", "destination_path", "file_name")
