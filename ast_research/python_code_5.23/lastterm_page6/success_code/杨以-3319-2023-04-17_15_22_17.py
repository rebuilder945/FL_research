n=eval(input())
lst=[]
for x in range(100,n+1):
    if (x%10)**3+((x//10)%10)**3+(((x//10)//10)%10)**3==x:
        print(x)
        lst.append(x)
if len(lst)==0:
        print('none')
