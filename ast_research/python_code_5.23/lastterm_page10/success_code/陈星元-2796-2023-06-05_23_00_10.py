def cutstr(str):
    str1=""
    for i in range(len(str)):
        if str[i].isdigit():
           str1+=str[i]
        else:
            str1+=" "
    ls=str1.split()
    return ls
str=input()
ls=cutstr(str)
if len(ls)==0:
    print("No digits")
else:
    ls.sort(key=lambda x:len(x))
    print(ls[-1])

            








