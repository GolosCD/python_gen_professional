'''
Популярные домены
Вам доступен файл data.csv, который содержит неповторяющиеся данные о пользователях некоторого ресурса. В первом столбце записано имя пользователя, во втором — фамилия, в третьем — адрес электронной почты:

first_name,surname,email
John,Wilson,johnwilson@outlook.com
Mary,Wilson,marywilson@list.ru
...
Напишите программу, которая создает файл domain_usage.csv, имеющий следующее содержание:

domain,count
rambler.ru,24
iCloud.com,29
...
где в первом столбце записано название почтового домена, а во втором — количество пользователей, использующих данный домен. Домены в файле должны быть расположены в порядке возрастания количества их использований, при совпадении количества использований — в лексикографическом порядке.

Примечание 1. Разделителем в файле data.csv является запятая, при этом кавычки не используются.

Примечание 2. Указанный файл доступен по ссылке. Ответ на задачу доступен по ссылке.

Примечание 3. Начальная часть файла domain_usage.csv выглядит так:

domain,count
rambler.ru,24
iCloud.com,29
...
Примечание 4. При открытии файла используйте явное указание кодировки UTF-8.

'''


import csv

file_name = 'data_domain.csv'

head = ['domain','count']
    
with open(file_name,'r',encoding='utf8') as file_open:
    file_read = csv.DictReader(file_open,delimiter=',', quotechar='"')
    dict_name = dict()
    for row in file_read:
        domain = row['email'][row['email'].index('@')+1:]
        dict_name[domain] = dict_name.get(domain,0)+1




with open('domain_usage.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(head)                 # запись заголовков
    for row in sorted(dict_name,key = lambda x: (dict_name[x],x)):                         # запись строк
        wr = list([row,dict_name.get(row)])
        writer.writerow(wr)