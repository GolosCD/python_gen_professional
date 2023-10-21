'''
Вам доступен файл name_log.csv, в котором находятся логи изменения имени пользователя. В первом столбце записано измененное имя пользователя, во втором — адрес электронной почты, в третьем — дата и время изменения. При этом email пользователь менять не может, только имя:

username,email,dtime
rare_charles6,charlesthompson@inbox.ru,15/11/2021 08:15
busy_patricia5,patriciasmith@bk.ru,07/11/2021 08:07
...
Напишите программу, которая определяет, сколько раз пользователь менял имя. Программа должна вывести адреса электронных почт пользователей, указав для каждого соответствующее количество смененных имен. Почтовые ящики должны быть расположены в лексикографическом порядке, каждый на отдельной строке, в следующем формате:

<адрес электронной почты>: <количество изменений имен>
Примечание 1. Начальная часть ответа выглядит так:

barbaraanderson@bk.ru: 3
barbarabrown@rambler.ru: 3
...
Примечание 2. Указанный файл доступен по ссылке. Ответ на задачу доступен по ссылке.

Примечание 3. При открытии файла используйте явное указание кодировки UTF-8.
'''

import csv
from collections import Counter

with open  ('name_log_COUNTER.csv','r',encoding = 'utf8') as open_file:
    emails_list = Counter(
                          sorted(
                                 [mini_dict.get('email') for mini_dict in csv.DictReader(open_file, delimiter=',', quotechar='"')]
                                 )
                         )

for key,val in emails_list.items():
    print(f'{key}: {val}')

