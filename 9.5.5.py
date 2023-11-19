def sort_priority(first:list,second:list)->callable:
    '''Функция сортирует списки и объединяет их в один.'''

    if len(globals().keys()) >14:
        tmp_name:str = list(globals().keys())[-1]
    else:
        tmp_name:str = list(globals().keys())[-2]

    exec(f'global {tmp_name}')

    tmp_second = [i for i in sorted(second) if i in first]
    tmp_first = [i for i in sorted(first)]

    first[:] = tmp_second+tmp_first

    # for elem in sorted(first):

    #     if not elem in tmp_second:

    #         tmp_second.append(elem)

    # globals()[f'{tmp_name}']=tmp_second

    


# numbers = [8, 3, 1, 2, 5, 4, 7, 6]
# group = {5, 7, 2, 3}
# sort_priority(numbers, group)

# print(numbers)
# print(len(globals().keys()))

# numbers = [150, 200, 300, 1000, 50, 20000]
# sort_priority(numbers, [300, 100, 200])

# print(numbers)
# [200, 300, 50, 150, 1000, 20000]

# TEST_5:
# data = list(range(0, 100, 5))
# sort_priority(data, {1, 90, 95, 25, 55, 64})

# print(data)
# TEST_5:
# print([25, 55, 90, 95, 0, 5, 10, 15, 20, 30, 35, 40, 45, 50, 60, 65, 70, 75, 80, 85])

numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {5, 7, 2, 3}
sort_priority(numbers, group)

print(numbers)

numbers = [150, 200, 300, 1000, 50, 20000]
sort_priority(numbers, [300, 100, 200])

print(numbers)

numbers = [9, 8, 7, 6, 5, 4, 3, 2, 1]
sort_priority(numbers, (300, 100, 200))

print(numbers)

numbers = list(range(100, -100, -1))
sort_priority(numbers, (98, 97, 100, 5, -9, -34))

print(numbers)

data = list(range(0, 100, 5))
sort_priority(data, {1, 90, 95, 25, 55, 64})

print(data)