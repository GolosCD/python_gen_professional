'''
Реализуйте генераторную функцию alternating_sequence(), которая принимает один аргумент:

count — натуральное число, по умолчанию имеет значение None
Если count имеет значение None, функция должна возвращать генератор, порождающий бесконечный знакочередующийся ряд натуральных чисел.

Если count имеет в качестве значения натуральное число, функция должна возвращать генератор, порождающий первые count чисел знакочередующегося ряда натуральных чисел, а затем возбуждающий исключение StopIteration.

Примечание 1. Знакочередующийся ряд натуральных чисел имеет вид: 1,−2,3,−4,5,−6,7,−8,9,−10,...
Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую генераторную  функцию alternating_sequence(), но не код, вызывающий ее.

Примечание 3. Тестовые данные доступны по ссылкам:
'''

def alt():
    while True:
        yield 1
        yield -1
           
def alternating_sequence(count = None):

    counter = 0
    my_mark = alt()
    
    while counter != count:
        counter+=1
        yield counter * next(my_mark)
            

# INPUT DATA:

# TEST_1:
generator = alternating_sequence()

print(next(generator))
print(next(generator))

# TEST_2:
generator = alternating_sequence(10)

print(*generator)

# TEST_3:
generator = alternating_sequence(100)

print(*generator)

# TEST_4:
generator = alternating_sequence(50)

for _ in generator:
    pass

try:
    next(generator)
except StopIteration:
    print('Error')

# TEST_5:
generator = alternating_sequence()

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

# TEST_6:
generator = alternating_sequence()

for _ in range(10_124_421):
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

# TEST_7:
generator = alternating_sequence(1)

try:
    print(next(generator))
    print(next(generator))
except StopIteration:
    print('Error')