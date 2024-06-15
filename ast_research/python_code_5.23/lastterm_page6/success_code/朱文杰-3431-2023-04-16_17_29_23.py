a=eval(input())
m=[]
n=[]
for i in range(1,11):
    if i%2!=0:
        m.append(i)
    else:
        n.append(i)
for i in range(11,19):
    if i%2!=0:
        n.append(i)
    else:
        m.append(i)
for i in range(19,29):
    if i%2!=0:
        m.append(i)
    else:
        n.append(i)
for i in range(29,37):
    if i%2!=0:
        n.append(i)
    else:
        m.append(i)
if a in m:
    print("red")
elif a in n:
    print("black")
elif a==0:
    print("green")
else:
    print("error")
