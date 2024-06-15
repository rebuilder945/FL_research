ls=input().split(" ")
s=ls[0]
ls.remove(s)
ls.sort(key=lambda x: int(x),reverse=True)
average=int((int(ls[0])+int(ls[1])+int(ls[2]))/3)
ls.append(average)
for i in ls:
    s=s+" "+str(i)
print(s)
