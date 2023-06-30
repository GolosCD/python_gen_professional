Функция saturdays_between_two_dates()
Реализуйте функцию saturdays_between_two_dates(), которая принимает два аргумента в следующем порядке:

start — начальная дата, тип date
end — конечная дата, тип date
Функция должна возвращать количество суббот между датами start и end включительно.

Примечание 1. Даты могут передаваться в любом порядке, то есть не гарантируется, что первая дата меньше второй.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию saturdays_between_two_dates(), но не код, вызывающий ее.

Примечание 3. Тестовые данные доступны по ссылкам:

from datetime import date   

date1 = date(2010, 6, 13)
date2 = date(2011, 7, 14)

def saturdays_between_two_dates(st,en):
    start = min(st,en)
    end  = max(st,en)
    
    if start>end:
        return []
    start = start.toordinal()
    end = end.toordinal()    
    
    suturday = 0   
    for i in range(end-start+1):
        if date.fromordinal(start+i).weekday()==5:
            suturday+=1
    return suturday
    
print(saturdays_between_two_dates(date1, date2))    