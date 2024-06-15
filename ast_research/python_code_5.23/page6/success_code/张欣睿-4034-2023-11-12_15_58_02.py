color1 = input()
color2 = input()
s1 = {color1,color2}
ps = {"red","blue"}
os = {"red","yellow"}
gs = {"blue","yellow"}
if s1 == ps:
    print("purple")
elif s1 == os:
    print("orange")
elif s1 == gs:
    print("green")
else:
    print("error")


