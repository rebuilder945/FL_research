a=eval(input())
b=a.copy()
for i in range(len(a)):
    if a[i]==0:
        b.remove(0)
        b.append(0)
    else:
        pass
print(b)



