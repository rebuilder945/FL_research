c1 = input()
c2 = input()
print(c1,c2)
p ={"red","blue"} 
o ={"red","yello"} 
g ={"yello","blue"} 
s = {c1,c2}
color = {"yello","blue","red"}
if c1 not in color or c2 not in color or c1==c2:
    print("error")
elif s == p:
    print("purple")
elif s == o:
    print("orange")
else:
    print("green")

