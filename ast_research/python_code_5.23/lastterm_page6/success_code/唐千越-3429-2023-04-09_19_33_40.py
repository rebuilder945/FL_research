lst = input()
a,b,c,d = 0,0,0,0
for x in lst:
    if x.isalpha(): #判断是不是字母
        a += 1
    elif x.isdigit(): #判断是不是数字
        b +=1
    elif x.isspace(): #判断是不是空格
        c += 1
    else:
        d += 1
print(a,c,b,d)

