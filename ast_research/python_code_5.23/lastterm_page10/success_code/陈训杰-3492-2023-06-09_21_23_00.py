s=input()
if s==None:
    print(None)
a=[]
for i in s:
    a=s.count(i)
    if a==1:
        print(i)
        break   
