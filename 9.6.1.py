# Реализуйте функцию get_digits() c использованием аннотаций типов, которая принимает один аргумент:

# number — положительное целое или вещественное число
# Функция должна возвращать список, состоящий из цифр числа number.

# Примечание 1. Используйте встроенные типы (list, tuple, ...), а не типы из модуля typing. Также используйте нотацию |, а не тип Union из модуля typing.

# Примечание 2. Порядок следования цифр в списке должен совпадать с порядком следования их в исходном числе.

# Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию get_digits(), но не код, вызывающий ее.


def get_digits(number: int|float)->list[int]:
    '''Функция принимает число и возвращает это числов виде списка элементов.'''
    
    return [int(i) for i in str(number) if i.isdigit()]


# INPUT DATA:

# TEST_1:
print(get_digits(16733))

# TEST_2:
print(get_digits(13.909934))

# TEST_3:
annotations = get_digits.__annotations__

print(annotations['return'])

# TEST_4:
annotations = get_digits.__annotations__

print(annotations['number'])

# TEST_5:
print(get_digits(848234124.73275))

# TEST_6:
print(get_digits(2))

# TEST_7:
print(get_digits(1234567890987654321))

# TEST_8:
print(*get_digits.__annotations__.keys())
print(*get_digits.__annotations__.values())