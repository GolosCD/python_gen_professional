import functools, time

def timer(iters=1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            total = 0
            for i in range(iters):
                start = time.perf_counter()
                value = func(*args, **kwargs)
                end = time.perf_counter()
                total += end - start
            print(f'Среднее время выполнения {func.__name__}: {round(total/iters, 4)} сек.')
            return value
        return wrapper
    return decorator




import timeit as ti


def mean(lst):
    return sum(lst) / len(lst)

test_data = (
    (1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
    (-3, -2, -1, 0, 1, 2, 3)
    # ('10', 20, 10),
    # (10, 20, 16, 18, '10'),
    # (10, 20, '16', 18, '10'),
    # tuple((10, 11, 12, 13, 14, 15, 16, 17, 18, 19, '42', 21, 22, 23, 24, 25, '42', 27, 28, 29, 30, '31', 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, '42', 43, 44, 45, 46, 47, '42', 49, 50, 51, 52, 53, 54, 55, 56, 57, '42', 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99)),
    # (3, 2, 1, -8, 1, 2, 3),
    # tuple(range(100, -1, -1)),
    # (11, 20.7, 10),
    # [13] * 50
)

def serj(func):
    '''Декоратор - проверки значений передаваемой функции'''

    def inner(*args ,**kwargs ):
        
        #кидаю в сет, что бы не проверять дубли, а они есть
        total_set = ([*args,*kwargs.values()])

        if not all(map(lambda x: isinstance(x,int),total_set)):
            raise TypeError
        
        #вторая проверка всех значений не нужна. просто проверьте минимальное число
        elif min(total_set)<1:
            raise ValueError
        
        else:
            return func(*args,**kwargs)
                     
    return inner
    
    


def vlad(func):
    def wrapper(*args, **kwargs):
        for el in {*args, *kwargs.values()}:
            if isinstance(el, int):
                if el <= 0:
                    raise ValueError
            else:
                raise TypeError
        return func(*args, **kwargs)
    return wrapper
    
@timer(5)
@serj
def sej_positive_sum(*args):
    return sum(args)
    
@timer(5)    
@vlad
def vlad_positive_sum(*args):
    return sum(args)
    
    
for test in test_data:
    print(sej_positive_sum(test))
    print()
    print(vlad_positive_sum(test))


# vlad_code = """
# from __main__ import test


# def takes_positive(func):
    # def wrapper(*args, **kwargs):
        # for el in {*args, *kwargs.values()}:
            # if isinstance(el, int):
                # if el <= 0:
                    # raise ValueError
            # else:
                # raise TypeError
        # return func(*args, **kwargs)
    # return wrapper
    
    
# @takes_positive
# def positive_sum(*args):
    # return sum(args)
# """
# sergey_code = """
# from __main__ import test


# def takes_positive(func: callable):
    # def inner(*args,**kwargs):
        # кидаю в сет, что бы не проверять дубли, а они есть
        # total_set = set([*args,*kwargs.values()])

        # if not all(map(lambda x: isinstance(x,int),total_set)):
            # raise TypeError
        
        # вторая проверка всех значений не нужна. просто проверьте минимальное число
        # elif min(total_set)<1:
            # raise ValueError
        
        # else:
            # return func(*args,**kwargs)
                     
    # return inner
    
    
# @takes_positive
# def positive_sum(*args):
    # return sum(args)
# """
# try_code = """
# try:
    # positive_sum(*test)
# except:
    # pass
# """

# v_subtract_s = []
# v_better_s = []
# number = 10000
# for test in test_data:
    # print(f'test: {test}')
    
    # vlad_time = ti.timeit(try_code, setup=vlad_code, number=number)
    # sergey_time = ti.timeit(try_code, setup=sergey_code, number=number)
    # v_better_s.append(vlad_time < sergey_time)
    # v_subtract_s.append(vlad_time - sergey_time)
    
    # print(f'\tv<s: {v_better_s[-1]}')
    # print(f'\tv-s: {v_subtract_s[-1]}')
    

# print()
# print(f'mean(v<s): {mean(v_better_s)}')
# print(f'mean(v-s): {mean(v_subtract_s)}')