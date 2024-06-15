a,b = input().split(' ')
a=int(a)
b=int(b)
if b-a==3 and a>=0 and b>0:
    for i in range(a,b):
        for j in range(a,b):
            for x in range(a,b):
                if i!=j and i!=x and j!=x:
                    print(str(i)+str(j)+str(x),end=" ")
else:
    print('illegal input')
