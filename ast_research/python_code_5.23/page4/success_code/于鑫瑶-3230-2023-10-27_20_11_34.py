from audioop import reverse


ls1=eval(input())
ls1.sort(reverse=True)
m=""
for i in range(len(ls1)):
    m+=str(ls1[i])
print(int(m))


