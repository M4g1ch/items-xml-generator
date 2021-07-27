import re


wrong_ids_list = [str(i) for i in range(100, 26381)]


items = open('items12_v2.txt')
items_content = items.read()

items_list = items_content.split('\n')
items_list.pop()


items_dict = {}

for item in items_list:
    k, v = item.split('#')
    items_dict[k] = v

new_wrong_ids_list = []
missing_ids_list = []

for wrong_id in wrong_ids_list:
    if wrong_id not in items_dict:
        missing_ids_list.append(wrong_id)
    else:
        new_wrong_ids_list.append(wrong_id)


items_xml = open('items.xml')
lines = items_xml.readlines()
items_xml.close()

new_items_xml = open('items_v2.xml', 'w')

for line in lines:
    m = re.search('id="(\d+)"', line)
    if m:
        itemid = m.group(1)
    m2 = re.search('name="(\w+)"', line)
    if m2:
        name = m2.group(1)
    if m and m2 and itemid and name and itemid in new_wrong_ids_list:
        new_items_xml.write(line.replace(name, items_dict[itemid]))
    else:
        new_items_xml.write(line)

new_items_xml.close()

print(missing_ids_list)

