a=input()
a=a.strip("[")
a=a.rstrip("]")
b=[str(q) for q in a.split(",")]
lst = []
for el in b:
    if b.count(el) >= 1:
        b.remove(el)
print(lst) 
