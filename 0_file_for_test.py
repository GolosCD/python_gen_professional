string = 'bacde'

a = '''if hasattr(string, 'sort'):
    string.sort()'''

print(eval(a))
