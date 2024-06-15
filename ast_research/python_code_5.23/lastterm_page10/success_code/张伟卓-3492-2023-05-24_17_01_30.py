a=input()
for i in a:
    if a.count(i)==1:
        print(i)
        break
    elif a.isspace():
        print("None")
    elif a.count(i)>=1:
        pass
