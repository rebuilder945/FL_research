a=0
m=eval(input())
if m<=0:
    print('illegal input')
for i in range(m):
    n=str(m)
    if n[::-1]==n:
        print(m,end=' ')
        a+=1
if a==0:
    print('illegal input')


