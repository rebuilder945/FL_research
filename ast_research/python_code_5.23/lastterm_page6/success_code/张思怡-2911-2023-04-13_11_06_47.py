a=input()
b=[]
for i in range(len(a)):
    b.append(int(a[i]))
    print(b)
# b=input().split("")
# print(b)
for x in range(len(b)):
    b[x]=(b[x]+5)%10
    b.reverse()
    print(b)
for i in b:
    print(i,end="")
