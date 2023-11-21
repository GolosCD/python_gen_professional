'''
Реализуйте декоратор do_twice, вызывающий декорируемую функцию два раза.

Примечание 1. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции, а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый декоратор do_twice, но не код, вызывающий его. 
'''

input_params = str|list[str|int]

def do_twice (func: callable)-> callable:
    def decor_engine(*args: input_params,**kwargs: input_params)->callable:
        func(*args,**kwargs)
        a:str = func(*args,**kwargs)
        return a
    return decor_engine
    
@do_twice
def beegeek():
    print('beegeek')
    
print(beegeek())        