a=input()
num=[]
for x in a:
    t=(x+5)%10
    num.append(t)
num.sort(reverse=True)
print("".join(num))

