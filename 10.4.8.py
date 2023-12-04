'''
Итератор Cycle
Реализуйте класс Cycle, порождающий итераторы, конструктор которого принимает один аргумент:

iterable — итерируемый объект
Итератор класса Cycle должен циклично генерировать последовательность элементов итерируемого объекта iterable.

Примечание 1. Гарантируется, что итерируемый объект, передаваемый в конструктор класса, не является множеством и итератором.

Примечание 2. Элементы итерируемого объекта, генерируемые итератором, должны располагаться в своем изначальном порядке.

Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимый класс Cycle.
'''
class Cycle():

    def __init__(self,data):
        self.data = data
        self.len_data = len(data)
        self.counter = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.counter ==self.len_data:
            self.counter=0
            result = self.data[self.counter]
            self.counter +=1
            return result
        else:
            
            result = self.data[self.counter]
            self.counter+=1
            return result





# INPUT DATA:

# TEST_1:
cycle = Cycle('be')

print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))

# TEST_2:
cycle = Cycle([1])

print(next(cycle) + next(cycle) + next(cycle))

# TEST_3:
cycle = Cycle(range(100_000_000))

print(next(cycle))
print(next(cycle))

# TEST_4:
cycle = Cycle(range(10_000_000))

for _ in range(1000):
    next(cycle)

print(next(cycle))

# TEST_5:
cycle = Cycle('beegeek')

for _ in range(1000):
    next(cycle)

print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))

# TEST_6:
cycle = Cycle((0, 9, 8, 7, 6, 5, 5, 4, 3, 2, 1, 1, 2, 3, 4, 0, 9, 8, 87, 5666666))

for _ in range(2000):
    next(cycle)

print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))

# TEST_7:
cycle = Cycle((0,))

for _ in range(2000):
    next(cycle)

print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))

# TEST_8:
cycle = Cycle('B')

for _ in range(500):
    next(cycle)

print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))

# TEST_9:
cycle = Cycle('AJFHKJSDHFWIEFJIOFKDKSVNCVNJVDJSFNdfkdsjfiwej943257438j2j123')

for _ in range(666):
    next(cycle)

print(next(cycle))

# TEST_10:
cycle = Cycle([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

for _ in range(100):
    print(next(cycle))