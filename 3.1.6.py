Реализуйте функцию get_date_range(), которая принимает два аргумента в следующем порядке:

start — начальная дата, тип date
end — конечная дата, тип date
Функция get_date_range() должна возвращать список, состоящий из дат (тип date) от start до end включительно. Если start > end, функция должна вернуть пустой список.

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию get_date_range(), но не код, вызывающий ее.

Примечание 2. Тестовые данные доступны по ссылкам:

from datetime import date

date1 = date(2019, 6, 5)
date2 = date(2022, 6, 6)

def get_date_range(start,end):
    start = start.toordinal()
    end = end.toordinal()
    if start>end:
        return []
        
    result_date: list = list()    
    for i in range(end-start+1):
        result_date.append(date.fromordinal(start+i))
    return result_date         
            
print(*get_date_range(date1, date2), sep='\n')