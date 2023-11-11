def eval_func(lists:list)->list:
    if isinstance(lists,list):
        eva_val = eval("print(lists[-1])")
    elif isinstance(list,tuple):
        eva_val = eval("print(lists[0])")
    elif isinstance(list,set):
        eva_val = eval("print(len(lists))" )   
    return eva_val

eval_func([[1, 2], [3, 4], [5, 6]])
