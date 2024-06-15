a = eval(input())
n = []
for i in range(len(a)):
    n.append((int(a[i])+5)%10)
n.reverse()
print("".join(str(x)for x in n))
