def exchange(s):
    if "a"<=s<="z":
        s=chr(219-ord(s))
    elif "A"<=s<="Z":
        s=chr(155-ord(s))
    else:
        s=s
    return(s)
a=input()
print(a)
a=(" ".join(a)).split()
for x in a[:]:
    x=exchange(x)
    print(x,end="")
