x=eval(input())
list=[i for i in x]
n,m=eval(input())
if n>=len(list):
    print('error')
elif n<0 and abs(n)>len(list):
    print('error')
else:
    d=[list[n]]*m
    e=list+d
    print(e)



