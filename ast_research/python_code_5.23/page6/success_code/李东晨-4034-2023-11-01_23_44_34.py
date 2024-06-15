n=input("")
m=input("")
if n[0]!="r" and n[0]!="y" and n[0]!="b":
    print("error")
elif m[0]!="r" and m[0]!="y" and m[0]!="b":
    print("error")
elif n[0]==m[0]:
    print('error')
else:
    if n[0]=="r"and m[0]=="b":
        print("purple")
    if n[0]=="r" and m[0]=="y":
        print("orange")
    if n[0]=="b" and m[0]=="y":
        print("green")
