a=eval(input())
s=[]
for i in a:
    if i!=max(a) and i!=min(a):
        s.append(i)
print(s)
