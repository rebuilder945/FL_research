Str=input()
for i in Str:
    if Str.count(i)==1:
        print(i[:1])
        break
    else:
        print("None")
