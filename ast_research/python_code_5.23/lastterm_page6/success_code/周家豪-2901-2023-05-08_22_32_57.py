lst=[]

while True:
    a=input()
    if a=='#':
        break
    else:
        lst.append(int(a))

print(len(lst),sum(lst))
