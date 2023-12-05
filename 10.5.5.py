'''
Реализуйте генераторную функцию dates(), которая принимает два аргумента в следующем порядке:

start — дата, тип date
count — натуральное число, по умолчанию имеет значение None
Если count имеет значение None, функция должна возвращать генератор, порождающий последовательность 
из максимально допустимого количества дат (тип date), начиная с даты start.

Если count имеет в качестве значения натуральное число, функция должна возвращать генератор, порождающий 
последовательность из count дат (тип date), начиная с даты start, а затем возбуждающий исключение StopIteration.

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую генераторную функцию dates(), но не код, вызывающий ее.
'''
from datetime import date

def dates(start : date, count = None):
    year,month,day = start.year,start.month,start.day
    day-=1
    counter = 0
    
    while counter!=count:
        try:
            day+=1
            date(year,month,day)
        except:
            day=1
            month+=1
            if month>12:
                year+=1
                month=1
                if year>9999:
                    return StopIteration
                

        counter+=1
        yield date(year,month,day)
            



# INPUT DATA:

# TEST_1:
generator = dates(date(2022, 3, 8))

print(next(generator))
print(next(generator))
print(next(generator))

# TEST_2:
generator = dates(date(2022, 3, 8), 5)

print(*generator)

# TEST_3:
generator = dates(date(2025, 9, 11), 99)

print(*generator)

# TEST_4:
generator = dates(date(2024, 9, 13), 1)

try:
    d = next(generator)
    print(type(d))
    print(d)
    next(generator)
except StopIteration:
    print('Error')
    

# TEST_5:
generator = dates(date(2049, 1, 7))

for _ in range(10_000):
    next(generator)

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))


generator = dates(date(9999, 1, 7))

for _ in range(348):
    next(generator)

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))

try:
   print(next(generator))
except StopIteration:
    print('Error')
