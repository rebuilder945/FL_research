str1=input()
if str1=="":
    print("None")
else:
    for i in str1:
        if str1.count(i)>=2:
            str1=str1.replace(i,"")
        else:
            print(i)
            break
