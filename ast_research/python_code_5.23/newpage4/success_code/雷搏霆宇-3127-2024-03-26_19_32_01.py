n = int(input())
a = [i for i in range(1,n+1,1)]
for i in a:
    a.pop(0)
    a.append(i)
    if i == 1:
        break
print(a)




