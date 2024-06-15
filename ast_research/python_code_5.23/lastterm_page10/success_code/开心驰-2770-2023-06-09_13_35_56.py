a=input().split()
b=input().split()
c=0
for i in a:
    if a.count(i)==b.count(i):
        c+=1
if c==len(a):
    print("True")
else :
    print("False")    
    


    
