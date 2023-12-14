'''
Функция stop_on()
Реализуйте генераторную функцию, которая принимает два аргумента в следующем порядке:

iterable — итерируемый объект
obj — произвольный объект
Функция должна возвращать генератор, порождающий последовательность элементов итерируемого объекта iterable до тех пор, пока не будет достигнут элемент, равный obj. Если итерируемый объект iterable не содержит ни одного элемента, равного obj, генератор должен породить все элементы iterable.

Примечание 1. Элементы итерируемого объекта в возвращаемом функцией генераторе должны располагаться в своем исходном порядке.

Примечание 2. Гарантируется, что итерируемый объект, передаваемый в функцию, не является множеством.

Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию stop_on(), но не код, вызывающий ее.
'''

def stop_on(iterable,obj):
    
    for i in iterable:
        if i != obj:
            yield i
        else:
            break
            
            
    
    
    
    
    
# INPUT DATA:

# TEST_1:
numbers = [1, 2, 3, 4, 5]

print(*stop_on(numbers, 4))

# TEST_2:
iterator = iter('beegeek')

print(*stop_on(iterator, 'a'))

# TEST_3:
data = map(abs, range(-100, 100))

iterator = stop_on(data, 76)
# TEST_3:
# 100 99 98 97 96 95 94 93 92 91 90 89 88 87 86 85 84 83 82 81 80 79 78 77

print(*iterator)

# TEST_4:
data = map(str.upper, 'jhfjgshgkjfdjsgriyteryowpqerkelfsldfmnmnbmvcnmlgqweootiyoeytkldjhmvxcmkasd')

iterator = stop_on(data, 'o')

print(*iterator)

# TEST_5:
data = 'JSKFJSDIFjejfkdjKJFIOJfkgkSDJGIEJGsklGDnvmmcvlwoqeriwjndSKF'

iterator = stop_on(data, 'e')

print(*iterator)

# TEST_6:
data = 'g'

iterator = stop_on(data, 'g')

print(*iterator)

# TEST_7:
data = 'eeeeeeeeeeeeee'

iterator = stop_on(data, 'e')

print(*iterator)

# TEST_8:
data = iter('qweretqwewerqweqwerewr')

iterator = stop_on(data, 'H')

print(*iterator)

# TEST_9:
data = iter('beegeek')

iterator = stop_on(data, 'g')

print(next(iterator))
print(next(iterator))
print(next(iterator))

try:
    print(next(iterator))
except StopIteration:
    print('Error')

# TEST_10:
data = ['bee', 'geek', 'stepik', 'python']

print(*stop_on(data, 'stepik'))

# TEST_11:
data = []

print(list(stop_on(data, 'stepik')))