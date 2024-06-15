m=input()
n=input()
a=set(m,n)
q={"red","blue"}
w={"red","yellow"}
e={"blue","yellow"}
if a==q:
    print("purple")
elif a==w:
    print("orange")
elif a==e:
    print("green")
else:
    print("error")

