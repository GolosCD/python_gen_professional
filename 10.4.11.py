'''
Итератор Xrange 🌶️
Реализуйте класс Xrange, порождающий итераторы, конструктор которого принимает три аргумента в следующем порядке:

start — целое или вещественное число
end — целое или вещественное число
step — целое или вещественное число, по умолчанию имеет значение 1
Итератор класса Xrange должен генерировать последовательность членов арифметической прогрессии от start до end, включая start и не включая end, с шагом step, а затем возбуждать исключение StopIteration.

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимый класс Xrange.
'''
def my_range(start,end,step=1):
    seq = list()
    
    flag = True
    
    num = start

    while flag:
        seq.append(num)
        num = num+step
        if step>0:
            if num>=end:
                flag=False
        else:
            if num<=end:
                flag=False
    
    return seq 


class Xrange:

    def __init__(self,start,end,step=1):
        self.num = iter(my_range(start,end,step))
        self.counter = 0
        
    def __iter__(self):
        return self.num
    
    def __next__(self):
        try:
            return self.num
        except:
            raise StopIteration       

            
evens = Xrange(0, 10, 2)

print(*evens)

print()

xrange = Xrange(10, 1, -1)

print(*xrange)