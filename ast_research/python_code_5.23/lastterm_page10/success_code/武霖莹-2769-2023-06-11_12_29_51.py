m = input()
lst = []
for i in m:
    if "a"<= i <="z":
        t = ord(i)-ord("a")+1
        b = ord("z")-t+1
        lst.append(chr(b))
    elif "A"<= i <="Z":
        T = ord(i)-ord("A")+1
        B = ord("Z")-T+1
        lst.append(chr(B))
    else:
        lst.append(i)
print(m)
print("".join(lst))
