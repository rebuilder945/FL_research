def classify(a):
    if  a>=100 and a<=1000:   
        sum=0
        c=str(a)
        for i in c:
            i=int(i)
            sum+=i**3
        if a==sum:
            return True
b=eval(input())
d=[]
for x in range(100,b+1):
    if classify(x):
        d.append(x)
if len(d)==0:
    print("none")
else:
    for o in d:
        print(o)




