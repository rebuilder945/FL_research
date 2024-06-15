a=input()
b=input()
if b in a:
    for i in a:
        if i==b:
            lst=a.split(" ")
            lst.remove(i)
            break
    print(*lst)

