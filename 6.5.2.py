'''
Вам доступен список кортежей staff с данными о сотрудниках некоторой компании. Первым элементом кортежа является название отдела, вторым — имя и фамилия сотрудника, работающего в этом отделе.

Дополните приведенный ниже код, чтобы он определил, какое число сотрудников работает в каждом отделе и вывел названия всех отделов, указав для каждого соответствующее количество сотрудников. Отделы должны быть расположены в лексикографическом порядке, каждый на отдельной строке, в следующем формате:

<отдел>: <количество сотрудников>
Примечание. Начальная часть ответа выглядит так:

Accounting: 17
Developing: 7
'''

from collections import defaultdict

staff = [('Sales', 'Robert Barnes'), ('Developing', 'Thomas Porter'), ('Accounting', 'James Wilkins'), ('Sales', 'Connie Reid'), ('Accounting', 'Brenda Davis'), ('Developing', 'Miguel Norris'), ('Accounting', 'Linda Hudson'), ('Developing', 'Deborah George'), ('Developing', 'Nicole Watts'), ('Marketing', 'Billy Lloyd'), ('Sales', 'Charlotte Cox'), ('Marketing', 'Bernice Ramos'), ('Sales', 'Jose Taylor'), ('Sales', 'Katie Warner'), ('Accounting', 'Steven Diaz'), ('Accounting', 'Kimberly Reynolds'), ('Accounting', 'John Watts'), ('Accounting', 'Dale Houston'), ('Developing', 'Arlene Gibson'), ('Marketing', 'Joyce Lawrence'), ('Accounting', 'Rosemary Garcia'), ('Marketing', 'Ralph Morgan'), ('Marketing', 'Sam Davis'), ('Marketing', 'Gail Hill'), ('Accounting', 'Michelle Wright'), ('Accounting', 'Casey Jenkins'), ('Sales', 'Evelyn Martin'), ('Accounting', 'Aaron Ferguson'), ('Marketing', 'Andrew Clark'), ('Marketing', 'John Gonzalez'), ('Developing', 'Wilma Woods'), ('Sales', 'Marie Cooper'), ('Accounting', 'Kay Scott'), ('Sales', 'Gladys Taylor'), ('Accounting', 'Ann Bell'), ('Accounting', 'Craig Wood'), ('Accounting', 'Gloria Higgins'), ('Marketing', 'Mario Reynolds'), ('Marketing', 'Helen Taylor'), ('Marketing', 'Mary King'), ('Accounting', 'Jane Jackson'), ('Marketing', 'Carol Peters'), ('Sales', 'Alicia Mendoza'), ('Accounting', 'Edna Cunningham'), ('Developing', 'Joyce Rivera'), ('Sales', 'Joseph Lee'), ('Sales', 'John White'), ('Marketing', 'Charles Bailey'), ('Sales', 'Chester Fernandez'), ('Sales', 'John Washington')]

result_dict = defaultdict(int)

for price in staff:
    result_dict[price[0]]+=1
   
for key in sorted(result_dict,key = lambda x:x):
        print(f'{key}: {result_dict.get(key)}')
