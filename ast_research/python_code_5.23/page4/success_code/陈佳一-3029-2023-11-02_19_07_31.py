d=input()
b=eval(input())
a=d.split(",")
c=[[x,y] for x in a for y in b]
print(c)
