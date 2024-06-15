a=input()
b=input()
c=0
for x in range(len(a)):
    if a.count(a[x])==b.count(a[x]) and set(a)==set(b):
        c+=1
if c==len(a):    
    print('True')
else:
    print("False")
