from collections import ChainMap

fruits = ChainMap({'kiwi': 10, 'banana': 20},
                  {'lime': 10, 'pineapple': 15},
                  {'kiwi': 15, 'lime': 5})

print(*fruits.items())