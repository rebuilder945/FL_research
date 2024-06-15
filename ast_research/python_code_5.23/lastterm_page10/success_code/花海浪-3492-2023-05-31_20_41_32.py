str=input()
if str=='':
    print("None")
else:
    b=str
    for i in str:
        a=str.find(i)
        b=str[a+1:]
        if i not in b:
            print(i)
            break


