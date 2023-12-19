'''
Функция roundrobin() 🌶️
Реализуйте функцию roundrobin(), которая принимает произвольное количество позиционных 
аргументов, каждый из которых является итерируемым объектом.

Функция должна возвращать итератор, генерирующий последовательность из элементов всех переданных 
итерируемых объектов: сначала первый элемент первого итерируемого объекта, затем первый элемент второго 
итерируемого объекта, и так далее; после второй элемент первого итерируемого объекта, затем второй элемент второго 
итерируемого объекта, и так далее.

Примечание 1. Элементы итерируемых объектов в возвращаемом функцией итераторе должны располагаться в своем исходном порядке.

Примечание 2. Гарантируется, что итерируемый объект, передаваемый в функцию, не является множеством.

Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию roundrobin(), но не код, вызывающий ее.

Примечание 4. Тестовые данные доступны по ссылкам:
'''
import itertools as it

def roundrobin(*args):

    iterators_list :list = [iter(sequence) for sequence in args] 
        
    cycle_gen_list :list = it.cycle(iterators_list)
    
    while iterators_list:
        curent_sec = next(cycle_gen_list)
        try:
            yield next(curent_sec)
        except:
            iterators_list = [iter for iter in iterators_list if iter!=curent_sec]

    
    
    


# INPUT DATA:

# TEST_1:
print(*roundrobin('abc', 'd', 'ef'))

# TEST_2:
numbers = [1, 2, 3]
letters = iter('beegeek')

print(*roundrobin(numbers, letters))

# TEST_3:
print(list(roundrobin()))

# TEST_4:-ошибка (1 0 b 2 1 e 3 2 e 4 3 g 5 4 e 6 e 7 k 8 9 10)
numbers1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers2 = range(5)
letters = iter('beegeek')

print(*roundrobin(numbers1, numbers2, letters))

# TEST_5:
letters = iter('stepik')

print(*roundrobin(letters))

# TEST_6:
numbers = roundrobin(map(abs, range(-10, 10)))

print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))


# TEST_7: -ошибка (10 -10 5 -5 1 -1 9 -9 4 -4 0 8 -8 3 -3 7 -7 2 -2 6 -6 1 -1 5 -5 0 1 4 -4 1 2 3 -3 2 3 2 -2 3 4 1 -1 4 0 1 1 2 2 3 3 4 4 5 5 6 6 7 7 8 8 9 9)
numbers1 = map(abs, range(-10, 10))
numbers2 = filter(None, range(-10, 10))
numbers3 = map(abs, range(-5, 5))
numbers4 = filter(None, range(-5, 5))
numbers5 = map(abs, range(-1, 1))
numbers6 = filter(None, range(-1, 1))

print(*roundrobin(numbers1, numbers2, numbers3, numbers4, numbers5, numbers6))

# TEST_8:
print(list(roundrobin([], [], [], [])))

# TEST_9:
numbers = iter([1, 2, 3])
nones = iter([None, None, None, None])

print(*roundrobin(numbers, nones))

