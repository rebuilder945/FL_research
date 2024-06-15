s=input()
if s=="":
    print("None")
else:
    for i in s:
        if s.count(i)==1:
            print(i)
            break
    else:
        print("None")
