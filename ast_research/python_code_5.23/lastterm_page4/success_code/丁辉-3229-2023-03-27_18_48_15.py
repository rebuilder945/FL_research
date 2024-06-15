a=eval(input())
b=[]
for i in range(0,len(a),1):
    if a.count(a[i])==1:
        b.append(a[i])
        b.sort()
if b:
    print(",".join(map(str,b)))
else:
    print("False")
