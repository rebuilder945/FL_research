a=eval(input())
b,c=max(a),min(a)
d=[]
for i in a:
    if i!=b and i!=c:
        d.append(i)
print(d)
