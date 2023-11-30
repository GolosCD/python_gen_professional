st = set((3,2,1))
end = set((3,2))
string = 'beegeek'

from functools import reduce

def pl(a,b):
    return a+b


a = reduce(pl, [1,2,3])

print(a) #<<< 6


a = reduce(pl, [1,2,3],1)

print(a) #<<< 7