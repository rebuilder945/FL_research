ls = list(eval(input()))
n,m = eval(input())
ls2 = []
a = len(ls)
if not n>a-1 and n<-a:
    ls2.append(ls[n])
    ls3=ls2*m
    ls4=ls+ls3
    print(ls4)
else:
    print('error')

    

