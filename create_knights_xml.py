import lxml.etree as et
import xmltodict
import json

root_element = et.Element('knights')

with open('DATA/knights.txt') as knights_in:
    for raw_line in knights_in:
        line = raw_line.rstrip()
        name, title, color, quest, comment = line.split(':')

        knight_element = et.SubElement(root_element, "knight", title=title)
        name_element = et.SubElement(knight_element, "knight_name")
        name_element.text = name
        et.SubElement(knight_element, "color").text = color
        et.SubElement(knight_element, "quest").text =  quest
        et.SubElement(knight_element, "comment").text = comment

xml_doc = et.tostring(root_element, pretty_print=True, xml_declaration=True).decode()

print(xml_doc)

tree = et.ElementTree(root_element)
tree.write("knights.xml", pretty_print=True, xml_declaration=True)

data = xmltodict.parse(xml_doc)
print(f"{data = }")
print()

json_doc = json.dumps(data, indent=4)
print(json_doc)

