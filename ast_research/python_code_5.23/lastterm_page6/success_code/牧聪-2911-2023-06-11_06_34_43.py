a=input()
num=[]
for x in a:
    t=str((int(x)+5)%10)
    num.append(t)
num.reverse
print("".join(num))

