def max_integer(lst):   
    lst.sort(reverse=True)   
    num = ''    
    for i in lst:   
        num += str(i)   
    return int(num)
a=input()
b=a.split()
print(max_integer(b))
