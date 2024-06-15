a=0
m=eval(input())
if m<=0:
    print('illegal input')
for i in range(m):
    n=str(i)
    if n[::-1]==n:
        print(i,end=' ')
        a+=1
if a==0:
    print('illegal input')


