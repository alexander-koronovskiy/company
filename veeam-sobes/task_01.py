import xml.etree.ElementTree as ET

data = """<?xml version="1.0" encoding="UTF-8"?>
<config>
    <file />
    <file />
</config>
"""
myroot = ET.fromstring(data)
for x in myroot:
    print(str(x.tag))
