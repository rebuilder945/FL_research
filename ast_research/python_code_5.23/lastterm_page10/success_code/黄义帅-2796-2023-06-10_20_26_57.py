s=input()
count=0
Count=0
ls=[]
Ls=[]
for i in s:
    if i.isdigit():
        count+=1
        ls.append(i)
    else:
        if count>=Count:
            Count=count
            count=0
            Ls=ls.copy()
            ls=[]
        else:
            ls=[]
            count=0
if len(ls)>=len(Ls):
    result="".join(ls)
else:
    result="".join(Ls)
if len(result)>0:
    print(result)
else:
    print("No digits")
            




