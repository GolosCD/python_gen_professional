'''

Функция get_days_in_month()   
Реализуйте функцию get_days_in_month(), которая принимает два аргумента в следующем порядке:

year — натуральное число
month — полное название месяца на английском
Функция должна возвращать отсортированный по возрастанию список всех дат (тип date) месяца month и года year.

Примечание 1. Например, вызов:

get_days_in_month(2021, 'December')
должен вернуть список:

[datetime.date(2021, 12, 1), datetime.date(2021, 12, 2), ..., datetime.date(2021, 12, 30), datetime.date(2021, 12, 31)]
Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию get_days_in_month(), но не код, вызывающий ее.

Примечание 3. Тестовые данные доступны по ссылкам:
'''
from datetime import datetime,date
import calendar as cl


return_list = list()

def get_days_in_month(year: int,mon: str):
    
    mon = list(cl.month_name).index(mon)
    
    count_day = cl.monthrange(year,mon)[1]
    
    for num in range(1,count_day+1):
        return_list.append( date(year=year,month=mon,day = num))
        
    return return_list    