#Вам доступен текстовый файл files.txt, содержащий информацию о файлах. 
#Каждая строка файла содержит три значения, разделенные символом пробела — имя файла, 
#его размер (целое число) и единицы измерения:
#
#cant-help-myself.mp3 7 MB
#keep-yourself-alive.mp3 6 MB
#bones.mp3 5 MB
#...
#Напишите программу, которая группирует данные файлы по расширению, 
#определяя общий объем файлов каждой группы, и выводит полученные группы файлов, 
#указывая для каждой ее общий объем. Группы должны быть расположены в лексикографическом 
#порядке названий расширений, файлы в группах — в лексикографическом порядке их имен.

#data load
file_name: str = 'files.txt'

with open (file_name,'r',encoding='utf8') as file_open:
    load_list = [i.strip() for i in file_open.readlines()]

file_name: dict = dict()

total_size: dict = dict()

#функция перевода размеров в байты
def size_to_bite (dig: str,s: str):
    size_file = {'B': 1, 'KB': 1024, 'MB': 1048576, 'GB': 1073741824}
    return size_file.get(s) * int(dig)
    
#функция перевода в укрупненные еденицы измерения
def up_to_size(dig: int):
        if dig<1024:
            return f'{round(dig/1024)} B'
        elif dig//1024<1024:
            return f'{round(dig/1024)} KB'
        elif dig//1048576<1024:
            return f'{round(dig/1048576)} MB'
        elif dig//1073741824<1024:
            return f'{round(dig/1073741824)} GB'    
        
 
#prepare data
for file_info in load_list:
    file,size,unit = file_info.split()
    _,ex = file.split('.')
    
    total_size[ex] = total_size.get(ex,0)+size_to_bite(size,unit.strip())

    file_name[ex] = file_name.get(ex,[])+[file]
    
for key in sorted(total_size):
    print(*sorted(file_name.get(key)),sep='\n')
    print('----------')
    print('Summary:',up_to_size(total_size.get(key)))
    print()
