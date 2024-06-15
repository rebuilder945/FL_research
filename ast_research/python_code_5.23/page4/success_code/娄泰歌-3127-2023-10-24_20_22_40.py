def left_rotate_list(n):  
    lst = list(range(1, n+1))  
    lst.insert(0, lst.pop())  
    return lst 
 
n = int(input(""))  
print(left_rotate_list(n))
