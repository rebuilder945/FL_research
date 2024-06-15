numb=input()
length=len(numb)
for i in range(length):
    numb[i]=str((int(str(i))+5)%10)
for i in range(int(length/2)):
    numb[i][-i]=numb[-i][i]
