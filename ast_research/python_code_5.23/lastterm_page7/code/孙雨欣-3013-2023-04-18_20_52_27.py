dic={}
a=input()
if a=="ok":
    break
else:
    k,v=a.split(' ')
    dic[k]=int(v)
print(sorted(list(dic.keys())))
print(sorted(list(dic.values())))
if 'India' not in list(dic.keys()):
    print('no')  
else:
    print('yes')
print(sum(list(dic.values())))

