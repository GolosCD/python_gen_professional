import json

file_json = 'data.json'

result = list()

with open (file_json,'r',encoding ='utf8') as file_open:
    file_read = json.load(file_open)
    for key in file_read:
        if type(key) == str:
            result.append(key+'!')
        elif type(key) == int:
            result.append(key+1)
        elif type(key)== bool:
            key = not key
            result.append(key)
        elif type(key)== list:
            result.append(key*2)  
        elif type(key)== dict:
            key.setdefault('newkey',None)
            result.append(key)
        elif key is None:
            pass
        else:
            print(1)
    
with open ('updated_data.json','w',encoding = 'utf8') as write_file:
        write_file.write(json.dumps(result))
   