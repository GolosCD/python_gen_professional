def main ():
    a: int = 3
    
    return print(rec_fun(a))
    
    
def rec_fun(a: int,count:int =0) -> int:
        if a==10:
            return f'Остановка функции за {count} итераций'
        else:
            return rec_fun(a+1,count+1)
            
if __name__=='__main__':
    main()
           