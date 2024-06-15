x=eval(input())
list=[i for i in x]
n,m=eval(input())
if n>=len(list):
    print('error')
elif n<0 and abs(n)>len(list):
    print('error')
elif n<0 and abs(n)<=len(list):
    d=[list[n]]*m
    e=list+d
    print(e)
else:
    f=[list[n-1]]*m
    g=list+f
    print(g)



