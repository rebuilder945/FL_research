A=eval(input())
a=sum(A)/len(A)
if type(sum(A)%len(A)) is int:
    print(a)
else:
    print('{:.2f}'.format(a))

