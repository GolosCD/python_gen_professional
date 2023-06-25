en, ru = list('AaBCcEeHKMOoPpTXxy'), list('АаВСсЕеНКМОоРрТХху')

en_list = [ord (i) for i in en]

ru_list = [ord (i) for i in ru]

result = set()

for i in range(3):
    if ord(input()) in en_list:
        result.add('en')
    else:
        result.add('ru')

if len(result)==1:
    print(*result)
else:
    print('mix')
    
