a=input()
a=a.strip("[")
a=a.rstrip("]")
b=[q for q in a.split(",")]
lst = []
for el in b:
    if lst.count(el) < 1:
        lst.append(el)
print(lst) 
