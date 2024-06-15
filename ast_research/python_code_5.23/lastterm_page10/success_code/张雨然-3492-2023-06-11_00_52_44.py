s=input()
if not s :
    print("None")
else:
    for x in s:
        if s.count(x)==1:
            print(x)
            break

