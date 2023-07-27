'''
Лог-файл
Вам доступен файл name_log.csv, в котором находятся логи изменения имени пользователя. В первом столбце записано измененное имя пользователя, во втором — адрес электронной почты, в третьем — дата и время изменения. При этом email пользователь менять не может, только имя:

username,email,dtime
rare_charles6,charlesthompson@inbox.ru,15/11/2021 08:15
busy_patricia5,patriciasmith@bk.ru,07/11/2021 08:07
...
Напишите программу, которая отбирает из файла name_log.csv только самые свежие записи для каждого пользователя и записывает их в файл new_name_log.csv. В файле new_name_log.csv первой строкой должны быть заголовки столбцов такие же, как в файле name_log.csv. Логи в итоговом файле должны быть расположены в лексикографическом порядке названий электронных ящиков пользователей.

Примечание 1. Для части пользователей в исходном файле запись только одна, и тогда в итоговый файл следует записать только ее, для некоторых пользователей есть несколько записей с разными именами.

Например, пользователь с электронной почтой c3po@gmail.com несколько раз менял имя:

C=3PO,c3po@gmail.com,16/11/2021 17:10
C3PO,c3po@gmail.com,16/11/2021 17:15
C-3PO,c3po@gmail.com,16/11/2021 17:24
Из этих трех записей в итоговый файл должна быть записана только одна — самая свежая:

C-3PO,c3po@gmail.com,16/11/2021 17:24
Примечание 2. Разделителем в файле name_log.csv является запятая, при этом кавычки не используются.

Примечание 3. Указанный файл доступен по ссылке. Ответ на задачу доступен по ссылке.

Примечание 4. Начальная часть файла new_name_log.csv выглядит так:

username,email,dtime
angry-barbara2,barbaraanderson@bk.ru,17/11/2021 01:17
dead-barbara6,barbarabrown@rambler.ru,27/11/2021 08:27
busy_barbara7,barbaradavis@aol.com,24/11/2021 08:24
...
Примечание 5. При открытии файла используйте явное указание кодировки UTF-8.

'''


import csv
from datetime import datetime

file_name: str = 'name_log.csv'

with open (file_name, 'r', encoding = 'utf8',newline='') as file_open:
    
    header: list = ['username','email','dtime']
    
    file_read: dict = csv.DictReader(file_open,delimiter=',', quotechar='"')
    
    user_dict: dict = dict()
    
    for row_dict in file_read:
        
        user_name = row_dict['username']
        
        email = row_dict['email']
        
        date = datetime.strptime(row_dict['dtime'],'%d/%m/%Y %H:%M')
        
        user_dict[email] = user_dict.get(email,{})
        
        user_dict[email][date] = user_dict[email].get(date,[])+[user_name]       

with open ('new_name_log.csv','w',encoding='utf-8', newline='') as write_file:

    writer = csv.writer(write_file)
     
    writer.writerow(header)
    
    for key in sorted(user_dict,reverse = False):

        email = key
        
        last_date = max(user_dict.get(email))
        
        name = user_dict[email].get(last_date)
    
        
        writer.writerows([[*name,email,datetime.strftime(last_date,'%d/%m/%Y %H:%M')]])
        
        
А можно было так        

import csv

with open('name_log.csv') as file, open('new_name_log.csv', 'w') as out:
    data = sorted(csv.DictReader(file), key=lambda x: (x['email'], x['dtime']))
    d = {'columns': ['username', 'email', 'dtime']}
    for i in data:
        d[i['email']] = [i['username'], i['email'], i['dtime']]   
    new_data = csv.writer(out)
    new_data.writerows(d.values())