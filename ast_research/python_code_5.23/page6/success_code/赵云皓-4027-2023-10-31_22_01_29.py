a=[]
while not"#"in a:
    b=input()
    a.append(b)
a.remove("#")
a=list(map(int,a))
c=len(a)
d=sum(a)
print(c,d)

