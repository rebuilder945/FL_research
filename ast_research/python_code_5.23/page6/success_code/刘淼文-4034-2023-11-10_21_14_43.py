c1 = input()
c2 = input()
p ={"red","blue"} 
o ={"red","yellow"} 
g ={"yellow","blue"} 
s = {c1,c2}
color = {"yellow","blue","red"}
if c1 not in color or c2 not in color or c1==c2:
    print("error")
elif s == p:
    print("purple")
elif s == o:
    print("orange")
else:
    print("green")

