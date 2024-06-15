
b=[]
while True:
    a=input()
    if a=="#":
        break
    else:
        a=eval(a)
        if type(a)==int:
            b.append(a)
print(len(b),end=" ")
print(sum(b))


