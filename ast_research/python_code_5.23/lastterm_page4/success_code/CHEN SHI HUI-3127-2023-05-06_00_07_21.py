a=int(input())
lis=[x for x in range(1,a+1)]
b=lis[0]
lis.remove(b)
lis.append(b)

print(lis)

