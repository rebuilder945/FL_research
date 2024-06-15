a=[]
a.append("green")
for x in range(1,11):
    b="red"
    c="black"
    if x%2==0:
        a.append(c)
    elif x%2==1:
        a.append(b)
for x in range(11,19):
    b="black"
    c="red"
    if x%2==0:
        a.append(c)
    elif x%2==1:
        a.append(b)
for x in range(19,29):
    b="red"
    c="black"
    if x%2==0:
        a.append(c)
    elif x%2==1:
        a.append(b)
for x in range(29,37):
    b="red"
    c="black"
    if x%2==0:
        a.append(b)
    elif x%2==1:
        a.append(c)
r=eval(input())
if 0<=r<=36:
    print(a[r])
else:
    print("error")
