s=list(input())
mm=[0,0,0,0,0]
b=[]
for i in s:
    if "0"<=i<="9":
        mm[0]=1
    if "a"<=i<="z":
        mm[1]=1
    if "A"<=i<="Z":
        mm[2]=1
    if len(s)>=8:
        mm[3]=1
    if i in "~!@#$%^&*()_=-/,.?<>;[:{]}}\|":
        mm[4]=1
r=sum(mm)
print(r)
