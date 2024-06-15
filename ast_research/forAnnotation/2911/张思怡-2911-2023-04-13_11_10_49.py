a=input()
b=[]
for i in range(len(a)):
    b.append(int(a[i]))

# b=input().split("")
# print(b)
for x in range(len(b)):
    b[x]=(b[x]+5)%10
    b[0]=b[-1]
    b[1]=b[-2]
    # print(b)
for i in b:
    print(i,end="")
