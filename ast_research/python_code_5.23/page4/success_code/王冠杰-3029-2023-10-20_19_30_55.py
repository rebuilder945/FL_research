a=eval(input())
b=int(input())
c=a.split(",")
values=[]
for x in c:
    for y in b:
        values.append(x+y)
        print(values)

