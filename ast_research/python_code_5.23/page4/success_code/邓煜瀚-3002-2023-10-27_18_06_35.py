a=eval(input())
b=sum(a)
c=b/len(a)
if isinstance(c,int):
    print(round(c,1))
else:
    print(round(c,2))


