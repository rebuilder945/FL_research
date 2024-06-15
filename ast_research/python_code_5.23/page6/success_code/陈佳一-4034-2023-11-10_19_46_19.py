from stringprep import c22_specials


c1=input()
c2=input()
s1={c1,c2}
p={"red","blue"}
o={"red","yellow"}
g={"blue","yellow"}
if s1==p:
    print("purple")
elif s1==o:
    print("orange")
elif s1==g:
    print("green")
else:
    print("error")
