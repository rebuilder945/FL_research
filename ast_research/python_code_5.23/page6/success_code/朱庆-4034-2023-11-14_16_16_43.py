color1 = input()
color2 = input()
s1 = {color1,color2}
pset = {"red","blue"}
oset = {"red","yellow"}
gset = {"blue","yellow"}
sset = {"red","yellow","blue"}
if color1 not in sset or color2 not in sset or color1 ==color2:
    print("error")
elif s1 == pset:
    print("purple")
elif s1 ==oset:
    print("orange")
else:
    print("green")    
