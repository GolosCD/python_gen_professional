'''
Для дополнительного заработка Тимур решил заняться продажей овощей. У него имеются данные о продажах за год, разделенные на четыре файла по кварталам: quarter1.csv, quarter2.csv, quarter3.csv и quarter4.csv. В каждом файле в первом столбце указывается название продукта, а в последующих — количество проданного продукта в килограммах за определенный месяц:

продукт,январь,февраль,март
Картофель,39,61,3
Дайкон,51,96,83
...

Также присутствует файл prices.json, содержащий словарь, в котором ключом является название продукта, а значением — цена за килограмм в рублях:

{
   "Картофель": 53,
   "Дайкон": 55,
...
}

Напишите программу, которая выводит единственное число — сумму, заработанную Тимуром за год на продаже овощей.

Примечание 1. Ссылки на указанные файлы: quarter1.csv, quarter2.csv, quarter3.csv, quarter4.csv, prices.json. Ответ на задачу доступен по ссылке.

Примечание 2. При открытии файла используйте явное указание кодировки UTF-8.

'''

from collections import Counter
from collections import defaultdict
import csv
import json

fruit_and_price: dict =defaultdict(int)

with open ('prices.json','r',encoding = 'utf8') as json_file:
    price:dict = json.load(json_file)

for i in range(4):
    with open(f'quarter{i + 1}.csv','r',encoding = 'utf8') as open_file:

        for row in csv.DictReader(open_file):
            fruit_name = row.get('продукт')
            for key in row:
                if key!='продукт':
                    fruit_and_price[fruit_name]+=(int(row.get(key))*price.get(fruit_name))

print(Counter(fruit_and_price).total())