ls=input().split(" ")
s=ls[0]
ls.remove(s)
ls.sort(key=lambda x: int(x),reverse=True)
average="%.2f"%((int(ls[0])+int(ls[1])+int(ls[2]))/3)
for i in ls:
    s=s+" "+str("%.2f"%(int(i)))
s=s+" "+str(average)
print(s)
