str1=input()
if str1=="":
    print("None")
else:
    for i in str1:
        if str1.count(i)==1:
            print(i)
            break
    else:
        print("None")

