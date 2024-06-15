a=eval(input())
b=len(a)
c=sum(a)
d=c/b
e=c//d
if d==e:
    print(int(d))
elif d!=e:
    print("%.2f"% d )
