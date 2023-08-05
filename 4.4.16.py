import json

fr: str = 'food_services.json'

object: dict = dict()

with open (fr, 'r',encoding = 'utf8') as fo:

    for row_dict in sorted(json.load(fo), key = lambda x: x.get('SeatsCount'),reverse=False):

        type_object = row_dict.get('TypeObject')

        name_object = row_dict.get('Name')

        count = row_dict.get('SeatsCount')

        if name_object not in object:
            object[type_object] = f'{name_object}, {count}'
        else:
            continue    

for key in sorted(object,key= lambda x: x):
    print(f'{key}: {object.get(key)}')

#object.get(type_object,'')+
with open ('test_reverse.json','w',encoding ='utf8') as wr:
    wr.write(json.dumps(object,indent=3,ensure_ascii=False))
