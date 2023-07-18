'''
ТЧМ
Во многих музеях существует один день месяца, когда посещение музея для всех лиц или отдельных категорий граждан происходит без взимания платы. Например, в Эрмитаже это третий четверг месяца.

Напишите программу, которая определяет даты бесплатных дней посещения Эрмитажа в заданном году.

Формат входных данных
На вход программе подается натуральное число, представляющее год.

Формат выходных данных
Программа должна определить все даты бесплатных дней посещения Эрмитажа в введенном году и вывести их. Даты должны быть расположены в порядке возрастания, каждая на отдельной строке, в формате DD.MM.YYYY.

Примечание. Тестовые данные доступны по ссылкам:
'''

from datetime import datetime,date
import calendar as cl


return_list = list()

def get_all_mondays(year: int):
    
    for mon_num in range(1,13):
        c=0
        
        count_day = cl.monthrange(year,mon_num)[1]
    
        for num in range(1,count_day+1):
            
            days = date(year=year,month=mon_num,day = num)
            
            if days.weekday()==3:
                c+=1
                if c ==3:
                    return_list.append(days.strftime('%d.%m.%Y'))           
        
    return return_list  

print(*get_all_mondays(int(input())),sep='\n')