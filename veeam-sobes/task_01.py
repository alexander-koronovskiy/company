import shutil
import xml.etree.ElementTree as ET

root = ET.parse("config.xml").getroot()
for type_tag in root.findall("file"):
    src_path = type_tag.get("source_path")
    destination = type_tag.get("destination_path")
    f_name = type_tag.get("file_name")
    print(src_path + "\\" + f_name, destination)
