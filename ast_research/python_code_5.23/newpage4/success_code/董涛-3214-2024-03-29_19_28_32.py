f=eval(input())
s=f.count(0)
while f.count(0)>=1:
    f.remove(0)
m=[0]*s
f=f+m
print(f)
