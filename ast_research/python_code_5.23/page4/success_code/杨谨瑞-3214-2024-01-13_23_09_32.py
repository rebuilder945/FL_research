str1 = input()
li1 = list(map(int, str1[1:-1].split(',')))
li2=[]
for i in range(len(li1)):
    if li1[i]!=0:
        li2=li2+[li1[i]]
num1=len(li1)
num2=len(li2)
num3=num1-num2
for j in range(num3):
    li2+=[0]
print(li2)

