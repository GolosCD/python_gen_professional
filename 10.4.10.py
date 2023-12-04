'''
Реализуйте класс Alphabet, порождающий итераторы, конструктор которого принимает один аргумент:

language — код языка: ru — русский, en — английский
Итератор класса Alphabet() должен циклично генерировать последовательность строчных букв:

русского алфавита, если language имеет значение ru
английского алфавита, если language имеет значение en
Примечание 1. Буква ё в русском алфавите не учитывается.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый класс Alphabet.

Примечание 3. Тестовые данные доступны по ссылкам:
'''


class Alphabet:

    def __init__(self,language):
        self.language = language
        self.alphabet = range(ord('a'),ord('z')+1) if language == 'en' else range(ord('а'),ord('я')+1)
        self.num_alpha = -1
        
    def __iter__(self):
        return self
    
    def __next__(self):
        try:
            self.num_alpha += 1
            return chr(self.alphabet[self.num_alpha])
        except:
            self.num_alpha = 0
            return chr(self.alphabet[self.num_alpha])
            
            
# INPUT DATA:

# TEST_1:
ru_alpha = Alphabet('ru')

print(next(ru_alpha))
print(next(ru_alpha))
print(next(ru_alpha))

# TEST_2:
en_alpha = Alphabet('en')

letters = [next(en_alpha) for _ in range(28)]

print(*letters)

# TEST_3:
en_alpha = Alphabet('en')

for _ in range(100):
    print(next(en_alpha))

# TEST_4:
en_alpha = Alphabet('en')

for _ in range(1000):
    next(en_alpha)

print(next(en_alpha))

# TEST_5:
ru_alpha = Alphabet('ru')

for _ in range(1000):
    next(ru_alpha)

print(next(ru_alpha))

# TEST_6:
ru_alpha = Alphabet('ru')

for _ in range(50):
    print(next(ru_alpha))

# TEST_7:
ru_alpha = Alphabet('ru')

for _ in range(40):
    next(ru_alpha)

for _ in range(40):
    next(ru_alpha)

for _ in range(40):
    next(ru_alpha)

print(next(ru_alpha))

# TEST_8:
en_alpha = Alphabet('en')

for _ in range(40):
    next(en_alpha)

for _ in range(40):
    next(en_alpha)

for _ in range(40):
    next(en_alpha)

print(next(en_alpha))