a=input()
b=input()
c={a,b}
color1={"red","blue"}
color2={"red","yellow"}
color3={"yellow","blue"}
color={"purple","orange","green"}
if a not in color or b not in color:
    print("error")
if c==color1:
    print("purple")
if c==color2:
    print("orange")
if c==color3:
    print("green")

