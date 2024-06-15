a=eval(input())
b=[]
if a>1:
    for i in range(a):
        if i>=2:
            for j in range(2,i,1):
                if i%j==0:
                    break
            else:
                b.append(i)
    for x in b:
        if str(x)==str(x)[::-1]:
            print(x,end=' ')
else:
    print('illegal input')
