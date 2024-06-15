a=input()
l=len(a)
x1=0
x2=0
x3=0
x4=0
list1=[chr(i) for i in range(65,91)]
for x in range(97,123):
    b=chr(x)
    list1.append(b)
list2=[chr(32)]
list3=[chr(i) for i in range(48,58)]
for i in range(l):
    c=a[i]
    if c in list1:
        x1+=1
    elif c in list2:
        x2+=1
    elif c in list3:
        x3+=1
    else:
        x4+=1
print(x1,x2,x3,x4)
