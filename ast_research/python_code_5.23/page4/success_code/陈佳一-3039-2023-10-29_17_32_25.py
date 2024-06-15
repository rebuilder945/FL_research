a=eval(input())
b=max(a)
c=min(a)
a=[x for x in a if x!=b and x!=c]
print(a)
