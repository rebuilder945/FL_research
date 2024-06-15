n=input()
m=input()
ls=['red','blue','yellow']
if n==m or n not in ls or m not in ls:
    print("error")
else:
    if n=='red':
        if m=='blue':
            print("purple")
        elif m=='yellow':
            print("orange")
    elif n=='blue':
        if m=='red':
            print("purple")
        elif m=='yellow':
            print("green")
    elif n=='yellow':
        if m=='red':
            print("orange")
        elif m=='blue':
            print("green")



