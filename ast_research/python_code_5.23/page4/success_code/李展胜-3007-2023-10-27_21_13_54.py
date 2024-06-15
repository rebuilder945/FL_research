list=[eval(input())]
n,m=eval(input())
if n>len(list)-1 or m>len(list)-1:
    print('error')
else:
    list.remove(list(range(n,m,1))) 
    print(list)   

