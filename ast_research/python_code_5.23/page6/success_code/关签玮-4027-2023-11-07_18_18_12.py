lst=[]
while 1:
    a=input()
    if a!="#":
        lst.append(eval(a))
    if a=="#":
        break
print(len(lst),end=" ")
print(sum(lst))

