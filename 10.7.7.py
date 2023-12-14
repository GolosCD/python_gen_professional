'''
Функция txt_to_dict()
Вам доступен файл planets.txt, содержащий информацию о различных планетах. В первых четырех строках указаны характеристики первой планеты, после чего следует пустая строка, затем характеристики второй планеты, и так далее:

Name = Mercury
Diameter = 4879.4
Mass = 3.302×10^23
OrbitalPeriod = 0.241

Name = Venus
Diameter = 12103.6
Mass = 4.869×10^24
OrbitalPeriod = 0.615

...
Реализуйте генераторную функцию txt_to_dict(), которая не принимает никаких аргументов.

Функция должна возвращать генератор, порождающий последовательность словарей, каждый из которых содержит информацию об очередной планете из файла planets.txt, а именно ее название, диаметр, массу и орбитальный период. Например:

{'Name': 'Mercury', 'Diameter': '4879.4', 'Mass': '3.302×10^23', 'OrbitalPeriod': '0.241'}
Примечание 1. Указанный файл доступен по ссылке.

Примечание 2. При открытии файла используйте явное указание кодировки UTF-8.

Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию txt_to_dict(), но не код, вызывающий ее.
'''

# def txt_to_dict():
    # with open ('planets.txt','r',encoding = 'cp1251') as raw_file:
        # filter_1 = [[line.replace('\n',',')] for line in raw_file.read().split('\n\n')]
        # filter_2 = [[i.replace(' = ',',').split(',') for i in list_1[0].split(',')] for list_1 in filter_1]
        # filter_3 = [{v[0]:v[1] for v in el} for el in filter_2]
        # yield from filter_3

def txt_to_dict():
    with open ('planets.txt','r',encoding = 'cp1251') as raw_file:
        filter_1 = ([line.replace('\n',',')] for line in raw_file.read().split('\n\n'))
        filter_2 = ([i.replace(' = ',',').split(',') for i in list_1[0].split(',')] for list_1 in filter_1)
        filter_3 = ({v[0]:v[1] for v in el} for el in filter_2)
        yield from filter_3
        
        # for my_list in [[line.replace('\n',',')] for line in raw_file.read().split('\n\n')]:
            # mini_dict = dict()
            # for line in my_list[0].split(','):
                # mini_dict[line[0]] = mini_dict.get(line[0],'')+line[1]
                # yield line    
                # print(type(tuple(line.replace(' = ',','))))
            # yield mini_dict    
        
        
        # open_line = ([line.replace('\n',',')] for line in raw_file.read().split('\n\n'))        
        
        # for i in ((elem.replace(' = ',',') for tup in open_line for elem in tup[0].split(','))):
                # yield i
            
        # return my_tuple


a =txt_to_dict()

print(next(a))
print(next(a))
# print(next(a))
# print(next(a))

