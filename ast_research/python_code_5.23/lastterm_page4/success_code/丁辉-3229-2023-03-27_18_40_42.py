a=eval(input())
b=[]
for i in range(0,len(a),1):
    if a.count(i)==1:
        b.append(i)
        b.sort()
if b:
    print(",".join(map(str,b)))
else:
    print("False")
