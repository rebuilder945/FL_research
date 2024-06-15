s = input()
if s == "":
    print("None")
else:
    for c in s:
        if s.count(c) == 1:
            print(c)
            break
    else:
        print("None")
