a=eval(input())
b=sum(a)
c=b/len(a)
if isinstance(c,int):
    print(c)
else:
    print(round(c,2))


