num0=input()
num1=[]
for i in range(len(num1)):
    a=(int(num1[i])+5)%10
    num1.append(a)
num1.reverse()
print("".join(str(i)for i in num1))
