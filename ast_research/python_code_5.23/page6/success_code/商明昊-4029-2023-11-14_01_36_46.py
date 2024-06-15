import random
n,m=input().split()
n=eval(n)
m=eval(m)
if m-n!=3 or type(m)==float or type(n)==float or n<0:
    print('illegal input')
else:
    ls = [x for x in range(n,m)]
    ls2 = []
    for x in range(50):
        random.shuffle(ls)
        a=""
        for i in ls:
            a=a+str(i)
        b=str(a)
        if b not in ls2:
            ls2.append(b)
            ls2.sort()
        str1 = " ".join(ls2)
    print(str1)



