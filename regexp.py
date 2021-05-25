import re
from logger import logger
from settings import filepath

filepath = filepath()

@logger(filepath)
def normalize_fio(list):
    name = ','.join(list)
    pattern = r"(\w+)"
    result = re.findall(pattern, name)
    if len(result) < 3:
        result.append('')
    return result

@logger(filepath)
def normalize_phone(phone):
    pattern = r"((\+7|8)?\s*\(*(\d{3})\)*\s*\-*(\d{3})\-*(\d{2})\-*(\d{2}))\s*\(*([а-я.]+)*\s*(\d{4})*\)*"
    subs = r"+7(\3)\4-\5-\6 \7\8"
    result = re.sub(pattern, subs, phone)
    return result

@logger(filepath)
def duplicate_account(account, contact):
    if account[2] == '':
        account.insert(2, contact[2])
        account.pop(3)
    if account[3] == '':
        account.insert(3, contact[3])
        account.pop(4)
    if account[4] == '':
        account.insert(4, contact[4])
        account.pop(5)
    if account[5] == '':
        account.insert(5, contact[5])
        account.pop(6)
    if account[6] == '':
        account.insert(6, contact[6])
        account.pop()
    return account