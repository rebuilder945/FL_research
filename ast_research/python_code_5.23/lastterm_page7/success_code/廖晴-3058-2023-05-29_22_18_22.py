zi=[]
while True:
    count=0
    s=input()
    if s=='q':
        break
    else:
        zi.append(s)
cishu=[]
for i in zi:
    
    cishu.append(zi.count(i))
    maxi=max(cishu)
for x in zi:
    if zi.count(x)==maxi:
            print(x,maxi,end=" ")
            break

