import json


raw1 = 'data1.json'

raw2 = 'data2.json'

with open (raw1,'r',encoding = 'utf8') as open1,open (raw2,'r',encoding = 'utf8') as open2:
    dict_raw1 = json.load(open1)
    dict_raw2 = json.load(open2)
    
    dict_raw1.update(dict_raw2)
    
with open ('data_merge.json','w',encoding ='utf8') as wr:
    wr.write(json.dumps({key:dict_raw1.get(key) for key in sorted(dict_raw1,key = lambda x: x[0])}))
