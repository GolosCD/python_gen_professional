#Дневник космонавта 🌶️
#Вам доступен текстовый файл diary.txt, в который космонавт записывал небольшие отчёты за день. Каждый новый отчёт он мог записать либо в начало файла, либо в середину, либо в конец. Все отчеты разделены между собой пустой строкой. Каждый новый отчёт начинается со строки с датой и временем в формате DD.MM.YYYY; HH:MM, после которой следуют события, произошедшие за указанный день:
#
#29.04.2006; 06:55
#It wasn’t until several hours after launch that we were able to take the time to get out of our seats and enter the “habitation module.”
#Then, after another orbital maneuver, we finally were able to take a several hour break and get a little sleep.

#03.05.2006; 20:24
#Everybody had a sleeping bag although I only used mine on a couple of brief occasions, and then only when getting a little chilly.

#...
#Напишите программу, которая расставляет все записи космонавта в хронологическом порядке и выводит полученный результат.

from datetime import datetime

file_name = 'diary.txt'
with open (file_name, 'r', encoding = 'utf8') as open_file:
    raw_file = open_file.readlines()

dates_list:list = ' '.join(raw_file).split("\n \n ")

dates_dict:dict = {datetime.strptime(part[:17],'%d.%m.%Y; %H:%M'):part.replace('\n ','\n') for part in dates_list}


for key in sorted(dates_dict):
    print(dates_dict.get(key))
    print()
