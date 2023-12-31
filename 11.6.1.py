'''
Телефонные номера
Вам доступен набор телефонных номеров, имеющих следующие форматы:

<код страны>-<код города>-<номер>
<код страны> <код города> <номер>
в котором код страны и код города представлены последовательностями от одной до трех цифр включительно, а номер — последовательностью от четырех до десяти цифр включительно. 
Между кодом страны, кодом города и номером используется разделитель, которым служит либо символ дефис, либо пробел, причем одновременно оба вида разделителя в одном номере присутствовать не могут.

Напишите программу, которая принимает произвольное количество телефонных номеров и для каждого выводит отдельно его код страны, код города и номер.

Формат входных данных
На вход программе подается произвольное количество телефонных номеров, удовлетворяющих приведенным выше шаблонам, каждый на отдельной строке.

Формат выходных данных
Программа должна для каждого введенного телефонного номера вывести отдельно его код страны, код города и номер в следующем формате:

Код страны: <код страны>, Код города: <код города>, Номер: <номер>
'''

import re
import sys

input_text = [inp.strip() for inp in sys.stdin]

for search_text in input_text:
    match = re.search('(?P<cc>\d+)[- ](?P<ct>\d+)[- ](?P<number>\d+)?', search_text)
        
    code_country,code_town,code_number = match.groupdict().values()    
        
    print(f'Код страны: {code_country}, Код города: {code_town}, Номер: {code_number}')