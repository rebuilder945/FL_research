n = input()
b = [1+x for x in range(0,int(n))]
n = b.pop(0)
b.append(1)
print(b)
