import timeit as ti


def mean(lst):
    return sum(lst) / len(lst)

test_data = (
    (1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
    (-3, -2, -1, 0, 1, 2, 3),
    ('10', 20, 10),
    (10, 20, 16, 18, '10'),
    (10, 20, '16', 18, '10'),
    tuple(range(10, 100))+tuple(range(10, 100))+tuple('10'),
    (3, 2, 1, -8, 1, 2, 3),
    tuple(range(100, -1, -1)),
    (11, 20.7, 10),
    [13] * 50
)
vlad_code = """
from __main__ import test


def takes_positive(func):
    def wrapper(*args, **kwargs):
        for el in {*args, *kwargs.values()}:
            if isinstance(el, int):
                if el <= 0:
                    raise ValueError
            else:
                raise TypeError
        return func(*args, **kwargs)
    return wrapper
    
    
@takes_positive
def positive_sum(*args):
    return sum(args)
"""
sergey_code = """
from __main__ import test


def takes_positive(func: callable):
    def inner(*args,**kwargs):
        #кидаю в сет, что бы не проверять дубли, а они есть
        total_set = set([*args,*kwargs.values()])

        if not all(map(lambda x: isinstance(x,int),total_set)):
            raise TypeError
        
        #вторая проверка всех значений не нужна. просто проверьте минимальное число
        elif min(total_set)<1:
            raise ValueError
        
        else:
            return func(*args,**kwargs)
                     
    return inner
    
    
@takes_positive
def positive_sum(*args):
    return sum(args)
"""
try_code = """
try:
    positive_sum(*test)
except:
    pass
"""

v_subtract_s = []
v_better_s = []
number = 10000
for test in test_data:
    print(f'test: {test}')
    
    vlad_time = ti.timeit(try_code, setup=vlad_code, number=number)
    sergey_time = ti.timeit(try_code, setup=sergey_code, number=number)
    
    v_better_s.append(vlad_time < sergey_time)
    v_subtract_s.append(vlad_time - sergey_time)
    
    print(f'\tv<s: {v_better_s[-1]}')
    print(f'\tv-s: {v_subtract_s[-1]}')
    

print()
print(f'mean(v<s): {mean(v_better_s)}')
print(f'mean(v-s): {mean(v_subtract_s)}')