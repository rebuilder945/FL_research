a=eval(input())
b=[]
for x in range(0,len(a),1):
    if a.count(x)==1:
        b.append(x)
        b.sort()
        print(b)
    if a.count(x)!=1:
        print("False")

