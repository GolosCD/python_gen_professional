from collections import ChainMap

def deep_update(chainmap:dict,key:str,value:str):
    for minidict in chainmap.parents.maps:
        if key in minidict:
            minidict[key] = value
    return chainmap

chainmap = ChainMap({'city': 'Moscow'}, {'name': 'Arthur'}, {'name': 'Timur'})
deep_update(chainmap, 'name', 'Dima')

print(chainmap)