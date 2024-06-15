a=input()
b=a.split(",")
c=[]
d=eval(b[0])
for i in range(eval(b[1])):
    c.insert(i,d)
    d=d+eval(b[2])
print(c)
