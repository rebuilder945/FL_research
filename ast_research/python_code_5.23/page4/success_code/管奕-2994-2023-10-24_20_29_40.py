x=eval(input())
list=[i for i in x]
n,m=eval(input())
if n<len(list):
    a=[list[n-1]]
    b=a*m
    c=list+b
    print(c)
else:
    print('error')




