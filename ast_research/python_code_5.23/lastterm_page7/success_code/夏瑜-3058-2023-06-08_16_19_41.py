a=input() 
s1={}
b=0
while(a!="q"):
    s1[a]=s1.get(a,0)+1
    if s1[a]>b:
        b=s1[a]
    a=input() 
for f,v in s1.items():
    if v==b:
        print(f,v)
