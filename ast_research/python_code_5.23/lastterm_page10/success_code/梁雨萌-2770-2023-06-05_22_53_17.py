dic={}
str1 = input()
str2 = input()
for i in str1 :
    dic[i] = str1.count(i)
flag = True
for i in dic:
    if str2.count(i) != dic[i]:
        flag = False
        break
print(flag)
