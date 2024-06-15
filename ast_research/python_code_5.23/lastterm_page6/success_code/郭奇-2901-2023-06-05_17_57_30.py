lst=[]
while True:
    a=input()
    if a=='#':
        break
    else:
        s=int(a)
        lst.append(s)
print(len(lst),sum(lst))


