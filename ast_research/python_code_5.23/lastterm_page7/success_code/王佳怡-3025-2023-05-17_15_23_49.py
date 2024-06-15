a=input()
s=0
for x in a:
    if x!=" ":
        s+=1
l=a.split()
n=len(l)
b=s/n
print(n,end=",")
print("%.2f"%(b))
