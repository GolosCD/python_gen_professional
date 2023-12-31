'''
Спортивные площадки
Вам доступен файл playgrounds.csv с информацией о спортивных площадках Москвы. В первом столбце записан тип площадки,  во втором — административный округ, в третьем — название района, в четвертом — адрес:

ObjectName;AdmArea;District;Address
Парк, озелененная городская территория «Лианозовский парк культуры и отдыха»;Северо-Восточный административный округ;район Лианозово;Угличская улица, дом 13
...
Напишите программу, создающую JSON-объект, ключом в котором является административный округ, а значением — JSON-объект, в котором, в свою очередь, ключом является название района, относящийся к этому административному округу, а значением — список адресов всех площадок в этом районе. Полученный JSON-объект программа должна записать в файл addresses.json.

Примечание 1. Адреса в списках должны располагаться в своем исходном порядке.

Примечание 2. Разделителем в файле playgrounds.csv является точка с запятой, при этом кавычки не используются.

Примечание 3. Начальная часть файла addresses.json выглядит так:

{
   "Северо-Восточный административный округ": {
      "район Лианозово": [
         "Угличская улица, дом 13",
         "Алтуфьевское шоссе, дом 147А"
      ],
      "район Отрадное": [
         "Алтуфьевское шоссе, дом 20А",
         "Юрловский проезд, дом 8, строение 1",
         "Юрловский проезд, дом 8, строение 1"
      ],
      ...
   },
   ...
}
Примечание 4. Указанный файл доступен по ссылке. Ответ на задачу доступен по ссылке.

Примечание 5. При открытии файла используйте явное указание кодировки UTF-8.
'''

import csv
import json

raw: str = 'playgrounds.csv'

result_dict: dict = dict()

with open (raw,'r',encoding = 'utf8',newline='') as open_csv:

    csv_read = csv.reader(open_csv,delimiter = ';')
    
    next(csv_read)
    
    for x in csv_read:
  
        result_dict.setdefault(x[1], dict()).setdefault(x[2], []).append(x[3])

with open ('addresses.json','w',encoding = 'utf8') as wr:
    wr.write(json.dumps(result_dict,ensure_ascii=False))     
