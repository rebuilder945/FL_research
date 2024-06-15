a=input()
b=[]
for x in a:
    x=(int(x)+5)%10
    b.append(x)
for i in reversed(b):
    print(i,end='')
