list1=[]
while True:
    a=input()
    if a=="#":
        break
    else:
        a=int(a)
        list1.append(a)
print(len(list1),sum(list1))
