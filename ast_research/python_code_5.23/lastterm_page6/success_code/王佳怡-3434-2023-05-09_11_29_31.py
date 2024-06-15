c1=input()
c2=input()
s1={c1,c2}
p={"red","blue"}
o={"red","yellow"}
g={"blue","yellow"}
c={"red","blue","yellow"}
if c1 not in c or c2 not in c or c1==c2:
    print("error")
elif s1==p:
    print("purple")
elif s1==o:
    print("orange")
else:
    print("green")
