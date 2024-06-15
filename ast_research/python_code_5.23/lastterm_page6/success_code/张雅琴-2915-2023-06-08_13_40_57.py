a=eval(input())
lst=[]
for i in range(100,a+1):
    c=[]
    for j in range(0,len(str(i))):
        c.append(int(str(i)[j])**3)
    if sum(c)==a:        
        lst.append(i)
if len(lst)==0:
    print("none")
else:
    for i in lst:
        print(i)
