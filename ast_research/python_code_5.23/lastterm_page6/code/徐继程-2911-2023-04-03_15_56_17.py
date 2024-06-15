num=input()
numb=[]
number=0
for i in range(len(num)):
    numb.append(num[i])
length=len(numb)
for i in range(length):
    numb[i]=(int(numb[i])+5)%10
for i in range(int(length/2)):
    numb[i][-i]=numb[-i][i]
for i in range(len(num)):
    number=
print(numb)

