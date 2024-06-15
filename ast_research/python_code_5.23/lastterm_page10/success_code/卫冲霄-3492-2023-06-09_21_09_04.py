s=input()
if s=="":
    print("None")
else:
    for i in range(len(s)):
        if s.count(i)==1:
            print(i)
            break




