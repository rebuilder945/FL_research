
from re import A


a=list(eval(input()))
a.sort(reverse=True)
for i in a:
    if 0<=i<=9:
        print(i,end="")
    else:
        pass


