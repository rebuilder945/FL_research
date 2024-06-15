A=eval(input())
a=sum(A)/len(A)
if sum(A)%len(A)==0:
    print(a)
else:
    print('{:.2f}'.format(a))

