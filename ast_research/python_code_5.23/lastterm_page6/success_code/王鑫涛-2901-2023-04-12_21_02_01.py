a=[]
m=1
while (m):
    s=input()
    if (s!='#'):
        a.append(eval(input()))
    else:
        m=0
print(len(a),sum(a))
