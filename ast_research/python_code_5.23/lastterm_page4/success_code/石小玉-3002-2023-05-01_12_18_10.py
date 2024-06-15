lst=eval(input())
he=sum(lst)
pingjun=he/len(lst)
yushu=he%len(lst)
if yushu==0:
    print(int(pingjun))
else:
    print('%.2f'%(pingjun))


