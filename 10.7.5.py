'''
Функция years_days()
Реализуйте генераторную функцию years_days(), которая принимает один аргумент:

year — натуральное число
Функция должна возвращать генератор, порождающий последовательность всех дат (тип date) в году year.

Примечание 1. Возьмем в качестве примера 2022 год. В январе этого года 31 день, в феврале — 
28, в марте — 31, и так далее. Тогда генератор, полученный при вызове years_days(2022), должен порождать сначала все даты с 
1 по 31 января, затем с 1 по 28
28 февраля, и так далее до 31 декабря.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию years_days(), но не код, вызывающий ее.

Примечание 3. Тестовые данные доступны по ссылкам:
'''

from datetime import date,timedelta
from typing import Generator
from calendar import isleap


def years_days(years : int)->Generator:
    count_iteration = 365 + isleap(years)
    yield from (date(years,1,1)+timedelta(days = day) for day in range(count_iteration))
    
    
dates = years_days(2077)

print(*dates)