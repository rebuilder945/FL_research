color1=input()
color2=input()
s1={color1,color2}
topurple={"red","blue"}
toorange={"red","yellow"}
togreen={"blue","yellow"}
all={"yellow","red","blue"}
if color1 not in all or color2 not in all or color1==color2:
    print("error")
elif s1==topurple:
    print("purple")
elif s1==toorange:
    print("orange")
elif s1==togreen:
    print("green")
