a=input().split(' ')
b=input().split(' ')
q1 = eval(b[0])
q2 = eval(b[1])
if q1>=0 and q2>=0:
    w = [q1,q2]
elif q1>=0 and q2<0:
    w = [q1,q2+len(a)]
elif q1< 0 and q2>0:
    w = [q1+len(a),q2]
else:
    w = [q1+len(a),q2+len(a)]



e1 = int(max(w))
e2 = int(min(w))
R1=a.pop(e1)
R2=a.pop(e2)

a.insert(e2,R1)

a.insert(e1,R2)
print(a)
