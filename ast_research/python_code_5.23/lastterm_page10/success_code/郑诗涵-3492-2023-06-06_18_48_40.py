s=input()
if s:
    for i in s:
        if s.count(i)==1:
            print(1)
            break
    else:
        print("None")
else:
    print("None")
