str1=input()
str11=''
str2=input()
if len(str2)==1:
    for i in str1:
        if i!=str2:
            str11+=i
else:
    for i in range(len(str1)-len(str2)+1):
        str12=str1[i:i+len(str2)]
        if str12!=str2:
            str11+=i
print(str11)
