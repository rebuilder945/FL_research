num0=input()
num1=[]
for i in range(len(num1)):
    num1.append((int(num1[i])+5)%10)
num1.reverse()
print(" ".join(str(x) for x in num1))
