s=input()
a=0
d=0
k=0
o=0
for i in s:
    if i.isalpha():                           #判断是否为字母                        
        a=a+1
    elif i.isdigit():                   #判断是否为数字
        d=d+1
    elif i.isspace():                      #判断是否为空格
        k=k+1
    else:
        o=o+1
print(a,k,d,o)
