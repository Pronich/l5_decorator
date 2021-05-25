import csv
from pprint import pprint
from regexp import normalize_fio, normalize_phone, duplicate_account

if __name__ == '__main__':
    with open("phonebook_raw.csv") as f:
      rows = csv.reader(f, delimiter=",")
      contacts_list = list(rows)

    namelist = []
    phonebook = []

    for raw in contacts_list:
        contact = normalize_fio(raw[:3])
        contact.append(raw[3])
        contact.append(raw[4])
        if raw == contacts_list[0]:
            contact.append(raw[5])
        else:
            contact.append(normalize_phone(raw[5]))
        contact.append(raw[6])
        if ','.join(contact[:2]) in namelist:
            i = namelist.index(','.join(contact[:2]))
            account = duplicate_account(phonebook[i], contact)
            phonebook.pop(i)
            phonebook.append(account)
        else:
            namelist.append(','.join(contact[:2]))
            phonebook.append(contact)

    with open("phonebook.csv", "w") as f:
      datawriter = csv.writer(f, delimiter=',')
      datawriter.writerows(phonebook)