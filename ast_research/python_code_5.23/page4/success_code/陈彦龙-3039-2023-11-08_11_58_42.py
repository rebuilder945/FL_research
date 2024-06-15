ls1=eval(input())
s1=set(ls1)
ls1=list(s1)
a=max(ls1)
b=min(ls1)
ls1.remove(a)
ls1.remove(b)
print(ls1)

