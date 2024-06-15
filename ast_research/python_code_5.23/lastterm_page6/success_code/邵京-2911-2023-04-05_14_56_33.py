a=eval(input())
strnumbers=str(a)
for i in range(0,len(strnumbers)):
    strnumbers[i]=(int(strnumbers[i])+5)%10
strnumbers.reverse()
print(int(strnumbers))

