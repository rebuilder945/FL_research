str1=input()
print(str1)
for x in str1:
    if ord("a")<=ord(x)<=ord("z"):
        c=ord(x)-ord("a")+1
        k=26-c+1
        print(chr(ord("a")+k-1),end="")
    elif ord("A")<=ord(x)<=ord("Z"):
        c=ord(x)-ord("A")+1
        k=26-c+1
        print(chr(ord("A")+k-1),end="")
    else:
        print(x,end="")
