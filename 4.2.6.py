#Функция csv_columns()
#Реализуйте функцию csv_columns(), которая принимает один аргумент:
#
#filename — название csv файла, например, data.csv
#Функция должна возвращать словарь, в котором ключом является название столбца файла filename, а значением — список элементов этого столбца.
#
#Примечание 1. Гарантируется, что в передаваемом в функцию файле разделителем является запятая, при этом кавычки не используются.
#
#Примечание 2. Гарантируется, что у передаваемого в функцию файла первая строка содержит названия столбцов.
#
#Примечание 3. Например, если бы файл exam.csv имел вид:
#
#name,grade
#Timur,5
#Arthur,4
#Anri,5
#то следующий вызов функции csv_columns():
#
#csv_columns('exam.csv')
#должен был бы вернуть:

{'name': ['Timur', 'Arthur', 'Anri'], 'grade': ['5', '4', '5']}

import csv


def csv_columns(file_input:str):
    file_name = file_input
    
    with open(file_name,'r',encoding='utf8') as file_open:
        file_read = csv.DictReader(file_open,delimiter=',', quotechar='"')
        dict_name = dict()
        for row in file_read:
            for key in row:
                dict_name[key]=dict_name.get(key,[])+[row.get(key)]
        return dict_name        
    
   