str1 = input()
str2 = ''
a = 0
str3 = ''
b = 0
for i in str1:
    if i.isdigit():
        str2+=i
        a +=1
    else:
        if a>=b:
            b =a
            str3= str2
        a = 0
        str2 = ''
if a>=b:
    str3= str2
if len(str3)==0:
    print('No digits')
else:
    print(str3)
