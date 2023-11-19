'''
Реализуйте функцию top_grade() c использованием аннотаций типов, которая принимает один аргумент:

grades — словарь, содержащий данные об ученике, а именно имя по ключу name и список оценок по ключу grades
Функция должна возвращать словарь, содержащий имя ученика по ключу name и его самую высокую оценку по ключу top_grade.

Примечание 1. Используйте встроенные типы (list, tuple, ...), а не типы из модуля typing. Также используйте нотацию |, а не тип Union из модуля typing.

Примечание 2. В возвращаемом функцией словаре сначала должно следовать имя, а затем — самая высокая оценка.

Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию top_grade(), но не код, вызывающий ее.
'''

input_dict = dict[str, str | list[int]]

def top_grade(grades: input_dict)->dict[str, str | int]:

    return dict((('name',grades.get('name')),('top_grade',max(grades.get('grades')))))





# TEST_1:
info = {'name': 'Timur', 'grades': [30, 57, 99]}

print(top_grade(info))
# {'name': 'Timur', 'top_grade': 99}

# TEST_2:
print(top_grade({'name': 'Ruslan', 'grades': [19, 48, 86, 45, 32]}))

# TEST_3:
annotations = top_grade.__annotations__

print(annotations['grades'])

# TEST_4:
info = {'name': 'Artur', 'grades': [100, 28, 3, 97, 5]}
result = top_grade(info)

print(result)

# TEST_5:
info = {'name': 'Dima', 'grades': [99, 99, 99, 99, 99]}

print(top_grade(info))

# TEST_6:
info = {'name': 'Vlad', 'grades': [22, 22, 66, 66, 5]}

print(top_grade(info))

# TEST_7:
info = {'name': 'Egor', 'grades': [33, 33, 33, 64, 5]}

print(top_grade(info))

# TEST_8:
print(*top_grade.__annotations__.values())

# TEST_9:
info = {'name': 'Roman', 'grades': [40]}

print(top_grade(info))



# # TEST_1:
# {'name': 'Timur', 'top_grade': 99}

# # TEST_2:
# {'name': 'Ruslan', 'top_grade': 86}

# # TEST_3:
# dict[str, str | list[int]]

# # TEST_4:
# {'name': 'Artur', 'top_grade': 100}

# # TEST_5:
# {'name': 'Dima', 'top_grade': 99}

# # TEST_6:
# {'name': 'Vlad', 'top_grade': 66}

# # TEST_7:
# {'name': 'Egor', 'top_grade': 64}

# # TEST_8:
# dict[str, str | list[int]] dict[str, str | int]

# # TEST_9:
# {'name': 'Roman', 'top_grade': 40}