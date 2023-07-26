'''
Последний день на Титанике
Вам доступен файл titanic.csv, который содержит данные о пассажирах, присутствовавших на борту парохода Титаник. В первом столбце указана единица, если пассажир выжил, и ноль в противном случае, во втором столбце записано полное имя пассажира, в третьем — пол, в четвертом — возраст:

survived;name;sex;age
0;Mr. Owen Harris Braund;male;22
1;Mrs. John Bradley (Florence Briggs Thayer) Cumings;female;38
...
Напишите программу, которая выводит имена выживших пассажиров, которым было менее 
18
18 лет, каждое на отдельной строке. Причем сначала должны быть расположены имена всех пассажиров мужского пола, а затем — женского, имена же непосредственно в мужском и женском списках должны быть расположены в своем исходном порядке.

Примечание 1. Разделителем в файле titanic.csv является точка с запятой, при этом кавычки не используются.

Примечание 2. Указанный файл доступен по ссылке. Ответ на задачу доступен по ссылке.

Примечание 3. Часть ответа выглядит так:

Master. Gerios Moubarek
Master. Alden Gates Caldwell
...
Master. Harold Theodor Johnson
Mrs. Nicholas (Adele Achem) Nasser
Miss. Marguerite Rut Sandstrom
...
Примечание 4. При открытии файла используйте явное указание кодировки UTF-8.
'''


import csv

peoples: dict = dict()
    
with open('titanic.csv', 'r',encoding = 'utf8') as file:

    for row in csv.DictReader(file,delimiter=';', quotechar='"'):
        age = float(row['age'])
        flag = row['survived']
        
        if flag == '1' and age <18.0:
            sex = 1 if row['sex']=='male' else 0
            name = row['name']
            if flag == '1' and age <=18.0:
                peoples[name] = sex
        else:
            continue        

print(*sorted(peoples,key = lambda x: peoples[x],reverse=True),sep='\n') 