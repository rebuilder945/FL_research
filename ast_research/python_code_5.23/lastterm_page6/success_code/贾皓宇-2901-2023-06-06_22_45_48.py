lst=[]
while True:
    a=input()
    if a==('#'):
        print(len(lst),sum(lst))
        break
    else:
        lst.append(int(a))


