a = list(input())

for i in range(len(a)):
    a[i]= (int(a[i])+5)%10
a = list(map(str,a))
s = "".join(a)
print(s)
