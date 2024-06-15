s=eval(input())
a=max(s)
b=min(s)
s1=s.copy()
for i in s:
    if i==a or i==b:
        s1.remove(i)
print(s1)
