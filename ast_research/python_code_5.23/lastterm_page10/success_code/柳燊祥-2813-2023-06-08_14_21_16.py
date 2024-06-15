a=input()
b=input()
lst1=list(a)
lst2=list(b)
while True:
    for x in lst2:
        if x in lst1:
            lst1.remove(x)
    break
print("".join(lst1))
