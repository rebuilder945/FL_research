v = list(eval(input()))
print(v)
v.reverse()
v1=[]
for x in v:
    if x not in v1:
        v1,insert(0,x)
print(v1)
