s=input() or "None"
if s =="None":
    print(s)
else:
    for x in s:
        if s.count(x) ==1:
            print(x)
            break
