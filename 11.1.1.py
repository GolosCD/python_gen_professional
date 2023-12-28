'''
Я в аду?
Напишите программу, которая в заданном тексте находит все телефонные номера, соответствующие следующим форматам:

7-ddd-ddd-dd-dd
8-ddd-dddd-dddd
где d — цифра от 0 до 9.


Формат входных данных
На вход программе подается строка произвольного содержания.

Формат выходных данных
Программа должна в введенном тексте найти все телефонные номера, соответствующие форматам, указанным в условии задачи, и вывести их в том порядке, в котором они были найдены, каждый на отдельной строке.

Примечание. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

Перезвони мне, пожалуйста: 7-919-667-21-19
Sample Output 1:

7-919-667-21-19
Sample Input 2:

Артур: +7-919-667-21-19, Анри: 7-hey-anri-anri, Тимур: 8-917-4864-1911
Sample Output 2:

7-919-667-21-19
8-917-4864-1911
'''

txt = 'Артур: +7-919-667-21-19, Анри: 7-hey-anri-anri, Тимур: 8-917-4864-1911'

txt_list = txt.split()

# print(txt_list)

# print(len('7-ddd-ddd-dd-dd'))

for line in txt_list:
    first_val = line[0] if line[0]!='+' else line[1]
    print('===========================================')
    print(first_val,first_val.isdigit())
    if first_val.isdigit():
        tmp_number = line[0:15 if line[0].isdigit() else 16]
        print('tmp_number: ',tmp_number)
        
        last_val = tmp_number[-1]
        
        print('last_val: ',last_val)
        count = tmp_number.count('-')
        print('count: ',count)
        
        if last_val.isdigit():
            print('last for>>>>')
            if count in (3,4):
                print('ANSWERS',tmp_number)
                
for line in txt_list:
    first_val = line[0]

    if first_val.isdigit():
        tmp_number = line[0 if line[0].isdigit() else 1:15 if line[0].isdigit() else 16]
        
        last_val = tmp_number[-1]

        count = tmp_number.count('-')

        
        if last_val.isdigit():
            if count in (3,4):
                print('****',tmp_number)                

# INPUT DATA:

# TEST_1:
# Перезвони мне, пожалуйста: 7-919-667-21-19

# TEST_2:
# Артур: +7-919-667-21-19, Анри: 7-hey-anri-anri, Тимур: 8-917-4864-1911

# TEST_3:
# Тимур: 7-ddd-ddd-dd-dd, Сослан: 8-ddd-dddd-dddd, Артур: 7-123-123-11-22,,,, Дима: 8-123-123-11-22, Анри: 8-123-1231-1221...... Гвидо: 7-123-1231-1221, 7-123-13-181-22, 8-1237-131-1221