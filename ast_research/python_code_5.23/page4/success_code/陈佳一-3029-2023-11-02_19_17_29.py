d=input()
b=eval(input())
a=d.split(",")
for n in range(0,3):
    c=[[x,y] for x in a[n] for y in b[n]]
print(c)
