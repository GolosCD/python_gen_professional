'''
Проще, чем кажется 🌶️
Рассмотрим следующий текстовый фрагмент:

ball,color,purple
ball,size,4
ball,notes,it's round
cup,color,blue
cup,size,1
cup,notes,none
Каждая строка этого фрагмента содержит три значения через запятую: имя объекта, свойство этого объекта, значение свойства. Например, в первой строке указан объект ball, имеющий свойство color, значение которого равно purple. Также у объекта ball есть свойства size и notes, имеющие значения 4 и it's round соответственно. Помимо объекта ball имеется объект cup, имеющий те же свойства и в том же количестве. Дадим этим объектам общее название object и сгруппируем строки данного текстового фрагмента по первому столбцу:

object,color,size,notes
ball,purple,4,it's round
cup,blue,1,none
Мы получили запись в привычном CSV формате, в котором в первом столбце указывается имя объекта, а в последующих — значения соответствующих свойств этого объекта.

Реализуйте функцию condense_csv(), которая принимает два аргумента в следующем формате:

filename — название csv файла, например, data.csv; формат содержимого файла аналогичен формату текстового фрагмента, рассмотренного в условии задачи: каждая строка файла содержит три значения через запятую, а именно имя объекта, свойство этого объекта, значение свойства; все объекты имеют равные свойства и в равных количествах
id_name — общее название для объектов
Функция должна привести содержимое файла в привычный CSV формат, сгруппировав строки по первому столбцу и назвав первый столбец id_name. Полученный результат функция должна записать в файл condensed.csv.

Примечание 1. Например, если бы файл data.csv имел следующий вид:

01,Title,Ran So Hard the Sun Went Down
02,Title,Honky Tonk Heroes (Like Me)
то вызов функции condense_csv():

condense_csv('data.csv', id_name='ID')
должен был бы создать файл condensed.csv со следующим содержанием:

ID,Title
01,Ran So Hard the Sun Went Down
02,Honky Tonk Heroes (Like Me)
Примечание 2. Гарантируется, что в передаваемом в функцию csv файле разделителем является запятая, при этом кавычки не используются.

Примечание 3. При открытии файла используйте явное указание кодировки UTF-8.

Примечание 4. В тестирующую систему сдайте программу, содержащую только необходимую функцию condense_csv(), но не код, вызывающий ее.

Примечание 5. Тестовые данные доступны по ссылкам:
'''
import csv

def condense_csv (file: str, id_name:str):

    file_name = file
        
    dict_file: dict = dict()
    
    #читаем файл
    with open (file_name,'r',encoding='utf8',newline='') as file_open:
    
        file_read = list(csv.reader(file_open,delimiter=','))
    # создаем словарь из полученных данных    
        for row in file_read:
            
            id_row = row[0]
            
            title_row = row[1]
            
            text_row = row[2]
            
            dict_file[id_row] = dict_file.get(id_row,dict())
            
            dict_file[id_row][title_row] = dict_file[id_row].get(title_row,list())+[text_row]
            
    # создаем заголовок        
    header = [id_name]
    
    first_key = list(dict_file.keys())[0]        
    
    
    header +=list(dict_file.get(first_key).keys())
    
    
    #создаем ключи
    
    #сохраняем результат в файл
    with open ('condensed.csv','w',encoding='utf8',newline='') as write_file:
        
        writer = csv.writer(write_file)
        
        writer.writerow(header)
        
        for key in dict_file:
            
            resuslt_list: list = list([key])
            
            for items in header[1:]:
                resuslt_list+=dict_file.get(key).get(items)
            
            writer.writerows([resuslt_list])
        
        
                
        
# От Гудкова

Дмитрий Гудков
7 месяцев назад
:)

Верное решение #854528041
Python 3.10
import csv

def condense_csv(filename, id_name='ID', d={}):
    title = [id_name]
    with open(filename, encoding='utf-8') as file, open('condensed.csv', 'w', newline='') as out:
        for i in csv.reader(file):
            d.setdefault(i[0], {}).update({i[1]: i[2]})
            if i[1] not in title:
                title.append(i[1])
        writer = csv.writer(out)
        writer.writerow(title)
        [writer.writerow([i, *d[i].values()]) for i in d]       