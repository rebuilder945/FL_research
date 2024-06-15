n=input()
ls={}
m=0
for i in n:
    ls[i]=ls.get(i,0)+1

for x,y in ls.items():
    if y==1:
        print(x)
        m+=1
        break
if n==""or m==0:
    print("None")
