a=input()
a=a.strip("[")
a=a.rstrip("]")
b=[eval(q) for q in a.split(",")]
for el in b:
    if b.count(el) >= 2:
        b.remove(el)
print(b) 
