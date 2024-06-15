a=eval(input())
b=0
lst=[]
for i in range(100,a+1):
    c=[]
    for j in range(0,len(str(i))):
        c.append(int(str(i)[j])**3)
    if sum(c)==a:
        b+=1
        lst.append(i)
if b==0:
    print("none")
else:
    for i in lst:
        print(i)
