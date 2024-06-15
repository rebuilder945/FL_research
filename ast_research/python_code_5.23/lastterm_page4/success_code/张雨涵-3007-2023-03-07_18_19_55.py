lst=eval(input())
n,m=eval(input())
if n>m :
    print("error")
else:
    for i in range(len(lst)):
        if n <m :
            del lst[n]
            n+=1
            continue
        else:
            break
    print(lst)
