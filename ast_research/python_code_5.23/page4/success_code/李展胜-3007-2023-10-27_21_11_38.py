list=[eval(input())]
n,m=eval(input())
if 'm'not in list or'n'not in list:
    print('error')
else:
    list.remove(list(range(n,m,1))) 
    print(list)   

