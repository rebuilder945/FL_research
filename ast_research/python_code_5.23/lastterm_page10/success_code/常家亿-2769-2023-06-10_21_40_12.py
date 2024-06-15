a=input()
lst1=[chr(x) for x in range(65,91)]
lst2=[chr(t)for t in range(97,123)]
print(a)
b=''
for x in a:
    if x.isalpha()==True:
        if x in lst1:
            i=lst1.index(x)
            x=lst1[25-i]
            b=b+x
        elif x in lst2:
            j = lst2.index(x)
            x=lst2[25-j]#replace只能从左往右替换，不能跳过左边第一个而替换后边的
            b=b+x
    else:
        b=b+x
print(b)
