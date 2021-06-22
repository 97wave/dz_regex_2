import re
import csv
from pprint import pprint

with open("phonebook_raw.csv", encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list_row = list(rows)
# pprint(contacts_list)
contacts_list = []
contacts_list.append(contacts_list_row[0])

for contact_row in contacts_list_row[1:]:
    fio = contact_row[0]
    contact = fio.split()
    
    if len(contact) == 1:
        fio = contact_row[1].split()
        if len(fio) == 1:
            contact.append(fio[0])
        else:
            contact.append(fio[0])
            contact.append(fio[1])

    if len(contact) == 2:
        contact.append(contact_row[2])
    contact.append(contact_row[3])
    contact.append(contact_row[4])

    phone_row = contact_row[5]
    if len(phone_row) >= 19:
        pattern_phone = r"(8|\+7)?\s*\(?(\d{3})\)?[-\s]*(\d{3})[-\s]*(\d{2})[-\s]*(\d{2})\s*\S*\s*(\d+)*\s*\W*\w*"
        sub = r"+7(\2)\3-\4-\5 доб.\6"
    else:
        pattern_phone = r"(8|\+7)?\s*\(?(\d{3})\)?[-\s]*(\d{3})[-\s]*(\d{2})[-\s]*(\d{2})"
        sub = r"+7(\2)\3-\4-\5"
    phone = re.sub(pattern_phone, sub, phone_row) 
    contact.append(phone)

    contact.append(contact_row[6])

    for double_contact in contacts_list:
        if contact[0] == double_contact[0] and contact[1] == double_contact[1]:
            for i in range(0, len(contact)):
                if double_contact[i] < contact[i]:
                    double_contact[i] = contact[i]  
    contacts_list.append(contact)

for contact in contacts_list:
    for double_contact in contacts_list:
        if double_contact[0] == contact[0] and double_contact != contact:
            contacts_list.remove(double_contact)

pprint(contacts_list)

with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(contacts_list)
