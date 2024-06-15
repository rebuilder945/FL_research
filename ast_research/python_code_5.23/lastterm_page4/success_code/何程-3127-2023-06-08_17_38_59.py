n=eval(input())
lst1=[n for n in range(1,n+1)]
jishu=0
a=0
for x in lst1:
    if jishu==0:
        a=x
        lst1[jishu]=lst1[jishu+1]
        jishu+=1
    elif jishu==len(lst1)-1:
        break
    else:
        lst1[jishu]=lst1[jishu+1]
        jishu+=1
lst1[jishu]=a
print(lst1)
