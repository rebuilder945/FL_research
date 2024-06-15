a = eval(input())
a.sort(reverse = True)
if max(a) == 0:
    print('0') 
else:
    b = list(map(str,a))
    print(*b)    
