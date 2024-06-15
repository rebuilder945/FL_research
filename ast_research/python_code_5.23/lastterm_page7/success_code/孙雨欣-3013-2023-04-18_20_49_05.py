dic={}
while True:
    a=input()
    if a=="ok":
        break
    else:
        k,v=map(int,a.split(''))
        dic[k]=v
    print(sorted(list(dic.keys())))
    print(sorted(list(dic.values())))
    if 'India' not in list(dic.keys()):
        print('no')  
    else:
        print('yes')
    print(sum(list(dic.values())))

