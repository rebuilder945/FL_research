x=0
a=[]
while x!='#':
    n=input()
    x=n
    if n!='#':
        a.append(n)
print(len(a),sum(map(int,a)))

