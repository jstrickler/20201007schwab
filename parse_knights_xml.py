import lxml.etree as et

doc = et.parse('knights.xml')

print(f"{doc = }")

# HARD WAY
root = doc.getroot()
print(f"{root = }")
for knight_element in root:  # loop over children of root element
    name_element = knight_element.find('knight_name')
    name = name_element.text
    print(f"{name = }")

print('-' * 60)

# EASY WAY
for knight_name in doc.findall('.//knight_name'):
    print(knight_name.text)