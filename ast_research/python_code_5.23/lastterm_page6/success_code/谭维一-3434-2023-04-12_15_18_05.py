c1=input()
c2=input()
s1 = {c1,c2}
p={"red","blue"}
g={"yellow","blue"}
o={"red","yellow"}
primary={"red","yellow","blue"}
if c1 not in primary or c2 not in primary or c1==c2:
    print("error")
elif s1==p:
    print("purple")
elif s1==g:
    print("green")
else:
    print("orange")
