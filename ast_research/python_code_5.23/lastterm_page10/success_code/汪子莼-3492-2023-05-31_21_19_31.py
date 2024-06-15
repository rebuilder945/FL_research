a=input()
ls=[]
for i in a:
    b=a.count(i)
    if b==1:
        ls.append(i)
if len(a)>=1:
    print(ls[0])
elif len(a)==0:
    print("None")
