id=input()
lstxishu="7-9-10-5-8-4-2-1-6-3-7-9-10-5-8-4-2".split("-")
sum=0
for i in range(len(id)-1):
    sum+=int(id[i])*int(lstxishu[i])
mod=sum%11
print("Correct" if id[17]==str((12-mod)%11) or (id[17]=="X" and (12-mod)%11==2) else "Wrong")

