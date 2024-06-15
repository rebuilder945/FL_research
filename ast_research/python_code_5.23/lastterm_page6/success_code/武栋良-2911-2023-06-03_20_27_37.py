n1=list(map(int,list(input())))
n2=[(x+5)%10 for x in n1]
n2.reverse()
s=''
for x in n2:
    s+=str(x)
print(s)




