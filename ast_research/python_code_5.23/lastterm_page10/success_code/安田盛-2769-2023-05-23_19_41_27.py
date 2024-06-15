s=input()
print(s)
for i in s:
    if ord("a")<=ord(i)<=ord("z"):
        print(chr(2*ord("a")+25-ord(i)),end="")
    elif ord("A")<=ord(i)<=ord("Z"):
        print(chr(2*ord("A")+25-ord(i)),end="")
    else:
        print(i,end="")



