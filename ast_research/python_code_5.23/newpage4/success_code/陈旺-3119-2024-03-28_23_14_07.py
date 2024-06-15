a=input()
a=a.strip("[")
a=a.rstrip("]")
b=[str(q) for q in a.split(",")]
for el in b:
    if b.count(el) >= 1:
        b.remove(el)
print(b) 
