a=input()
list1=a.split(",")
b=eval(input())
d=[]
for x in range(0,len(b)):
    c = [list1[x],b[x]]
    d.append(c)
print(d)

