'''
Онлайн-школа BEEGEEK
В онлайн-школе BEEGEEK логин учетной записи определяется следующим образом:

первым символом является символ нижнего подчеркивания _
затем следуют одна или более цифр
после записываются ноль или более латинских букв в произвольном регистре
логин может иметь на конце необязательный символ нижнего подчеркивания _
Напишите программу, которая принимает произвольное количество строк и определяет, какие из них представляют собой корректный логин онлайн-школы BEEGEEK.

Формат входных данных
На вход программе подаётся произвольное количество строк, каждая из которых содержит набор произвольных символов.

Формат выходных данных
Программа должна для каждой введенной строки вывести True, если она представляет собой корректный логин онлайн-школы BEEGEEK, или False в противном случае.
'''

import re
import sys

input_text = [txt.strip() for txt in sys.stdin]

for input_line in input_text:
    print(bool(re.fullmatch('^\_\d+[a-zA-Z]*\_{0,1}$',input_line)))