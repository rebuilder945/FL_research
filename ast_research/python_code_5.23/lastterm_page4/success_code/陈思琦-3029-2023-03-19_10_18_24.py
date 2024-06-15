a=input()
b=eval(input())
d=a.split(",")
print([[x,y] for x in d for y in b if d.index(x)==b.index(y)])
