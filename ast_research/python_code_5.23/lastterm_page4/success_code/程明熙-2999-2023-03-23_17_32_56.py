c=input()
x=list(input())
a=eval(x[0])
b=eval(x[-1])
l=c.split()
l[a],l[b]=l[b],l[a]
print(l)
# print(l)
