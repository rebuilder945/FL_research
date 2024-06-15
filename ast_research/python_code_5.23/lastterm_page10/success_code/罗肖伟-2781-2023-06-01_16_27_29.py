id=input()
id1=id[0:-1]
ls=[eval(x) for x in list(id1)]
lst=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
s=0
for i in range(len(ls)):
    s+=(ls[i]*lst[i])
n=s%11
m=(12-n)%11
if len(id)!=18:
    print("Error")
elif  m==10 and id[-1]=="X":
    print("Correct")
elif m==eval(id[-1]) and id[-1]!="X":
    print("Correct")
else:
    print("Wrong")
