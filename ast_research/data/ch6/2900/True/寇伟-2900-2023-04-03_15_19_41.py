n=eval(input())
ls=[]
if n>0 and n%int(n)==0:
    for i in range(2,n):
        if i==2:
            ls.append(i)
        for j in range(2,i):
            if i%j==0:
                break
            elif j==(i-1):
                if str(i)==str(i)[::-1]:
                    ls.append(i)


else:
    print('illegal input')
for i in ls:
    print(i,end=' ')
