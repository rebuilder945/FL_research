s=input()
print(s)
for i in s:
    if ord("a")<=ord(i)<=ord("z"):
        print(chr(2*ord("a")+26-ord(i)-1),end="")
    elif ord("A")<=ord(i)<+ord("Z"):
        print(chr(2*ord("A")+26-ord(i)-1),end="")
    else:
        print(i,end="")
