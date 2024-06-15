a=eval(input())
b=[max(a),min(a)]
c=a.copy()
for i in c:
    if i in b:
        a.remove(i)
print(a)

