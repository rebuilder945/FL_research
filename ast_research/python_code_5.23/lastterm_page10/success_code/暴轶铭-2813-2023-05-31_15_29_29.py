s1=input()#可自行添加提示语
s2=input()
flag=1
while flag==1:#若无子字符串在内则跳出循环
    flag=0
    if s2 in s1:
        s1=s1.replace(s2,'')
        flag=1
print(s1)


