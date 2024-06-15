a=input()
if a==("[]"):
    print("[]")
elif len(a)==1:
    a=a.strip("[")
    a=a.rstrip("]")
    b=[eval(q) for q in a.split(",")]
    b.sort()
    for i in range(int(b.count(b[0]))):
        b.remove(b[0])
    print(b)
else:
    a=a.strip("[")
    a=a.rstrip("]")
    b=[eval(q) for q in a.split(",")]
    b.sort()
    for i in range(int(b.count(b[0]))):
        b.remove(b[0])
    for i in range(int(b.count(b[-1]))):
        b.remove(b[-1])
    print(b)
