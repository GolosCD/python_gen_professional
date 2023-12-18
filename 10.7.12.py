'''
Функция around()
Реализуйте генераторную функцию, которая принимает один аргумент:

iterable — итерируемый объект
Функция должна возвращать генератор, порождающий последовательность кортежей, каждый из которых 
содержит очередной элемент итерируемого объекта iterable, а также предыдущий и следующий за ним элементы:

(<предыдущий элемент>, <очередной элемент>, <следующий элемент>)
Для первого элемента предыдущим считается значение None, для последнего элемента следующим считается так же значение None.

Примечание 1. Элементы итерируемого объекта в возвращаемом функцией генераторе должны располагаться в своем исходном порядке.

Примечание 2. Гарантируется, что итерируемый объект, передаваемый в функцию, не является множеством.

Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию around(), но не код, вызывающий ее.
'''
def around(iterable):
    iterable = list(iterable)
    for i in range(len(iterable)):
        if i == 0 and len(iterable) == 1:
            yield (None, iterable[i], None)
        elif i == 0:
            yield (None, iterable[i], iterable[i+1])    
        elif i == len(iterable) - 1:
            yield (iterable[i-1], iterable[i], None)
        else:
            yield (iterable[i-1], iterable[i], iterable[i+1])





# INPUT DATA:

# TEST_1:
numbers = [1, 2, 3, 4, 5]

print(*around(numbers))

# TEST_2:
iterator = iter('hey')

print(*around(iterator))

# TEST_3:
iterator = around(iter('beegeek'))

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
'''
# TEST_4:
data = map(abs, range(-100, 100))

print(*around(data))

# TEST_5:
data = map(str.upper, 'jhfjgshgkjfdjsgriyteryowpqerkelfsldfmnmnbmvcnmlgqweootiyoeytkldjhmvxcmkasd')

print(*around(data))

# TEST_6:
data = map(str.upper, 'y')

iterator = around(data)

print(next(iterator))

# TEST_7:
data = map(str.upper, 'yt')

print(*around(data))

# TEST_8:
data = map(str.upper, 'ytu')

print(*around(data))

# TEST_9:
data = ['bee', 'geek', 'stepik', 'python']

print(*around(data))
'''
# TEST_10:
print(list(around([])))
