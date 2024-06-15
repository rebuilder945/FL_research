str_lst=eval(input())
res={}
for stri in str_lst:
    for ch in stri:
        if ch in res:
            res[ch]+=1
        else:
            res[ch]=1
new_res=sorted(res.items(),key=lambda x:x[0])
for stri in new_res:
    print('%s,%d'%(stri[0],stri[1]))
