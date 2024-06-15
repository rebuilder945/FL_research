x=input()
a=[]
for i in range(len(x)):
    a.append(x[i])
r=0
b=[]
for s in range(len(a)):
    if a.count(a[s]) == 1:
        b.append(a[s])
        print(a[s])
        break
    else:
        r+=1
if len(b)== 0:
    print("None")
