ls=[]
while True:
    a=input()

    if a=='#':
        break
    ls.append(a)
ls=list(map(eval,ls))
print(len(ls),sum(ls))
