'''
Функция get_all_mondays()
Реализуйте функцию get_all_mondays(), которая принимает один аргумент:

year — натуральное число
Функция должна возвращать отсортированный по возрастанию список всех дат (тип date) года year, выпадающих на понедельник.

Примечание 1. Например, вызов:

get_all_mondays(2021)
должен вернуть список:

[datetime.date(2021, 1, 4), datetime.date(2021, 1, 11), ..., datetime.date(2021, 12, 20), datetime.date(2021, 12, 27)]
Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию get_all_mondays(), но не код, вызывающий ее.

Примечание 3. Тестовые данные доступны по ссылкам:
'''
from datetime import datetime,date
import calendar as cl


return_list = list()

def get_all_mondays(year: int):
    
    for mon_num in range(1,13):
        
        count_day = cl.monthrange(year,mon_num)[1]
    
        for num in range(1,count_day+1):
            
            days = date(year=year,month=mon_num,day = num)
            
            if days.weekday()==0:
                return_list.append(days)
        
    return return_list