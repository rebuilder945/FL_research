n = int(input())
ls1 = [x for x in range(1,n+1)]
ls2 = []
a = 1
for i in ls1:
    ls2.append(ls1[a])
    a+=1
    if a>len(ls1)-1:
        break
ls2.append(ls1[0])
print(ls2)
