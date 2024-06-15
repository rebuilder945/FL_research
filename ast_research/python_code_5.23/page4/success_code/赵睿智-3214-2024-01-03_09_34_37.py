a=input()
n=a.count(0)
for i in range(n):
    if i==0:
        a.pop(0)
        a.append(0)
print(a)

