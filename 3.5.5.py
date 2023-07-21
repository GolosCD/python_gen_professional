# Сотрудники организации 😄
# Дан список сотрудников организации, в котором указаны их фамилии, имена и даты рождения. Напишите программу, которая определяет самого старшего сотрудника из данного списка.

# Формат входных данных
# На вход программе в первой строке подается натуральное число 
# �
# n — количество сотрудников, работающих в организации. В последующих 
# �
# n строках вводятся данные о каждом сотруднике: имя, фамилия и дата рождения, разделённые пробелом. Дата рождения указывается в формате DD.MM.YYYY.

# Формат выходных данных
# Программа должна определить самого старшего сотрудника и вывести его дату рождения, имя и фамилию, разделив пробелом. Если таких сотрудников несколько, программа должна вывести их дату рождения, а также их количество, разделив пробелом.

# Примечание 1. Гарантируется, что у всех сотрудников имена и фамилии различны.

# Примечание 2. Тестовые данные доступны по ссылкам:

from datetime import datetime as dt
from datetime import timedelta as td

list_org = [input() for _ in range(int(input()))]

dict_name = dict()

for line in list_org:
    name,last,date = line.split()
    date = dt.strptime(date,'%d.%m.%Y')
    dict_name[date] = dict_name.get(date,[])
    dict_name[date].append(f'{name} {last}')

names = dict_name.get(min(dict_name))

print(min(dict_name).strftime('%d.%m.%Y'),*names if len(names)==1 else [len(names)])