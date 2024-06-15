a=input()
b=list(eval(input()))
c=a.split(",")
values=[]
for x in a:
    for y in c:
        values.append(x+y)
        print(values)

