dic={}
while True:
    a=input()
    if a=="q":
        break
    elif a in dic:
        dic[a]+=1
    else:
        dic[a]=1
list1=sorted(dic.items(),key=lambda x: x[1], reverse=True)

print('{} {}'.format(list1[0][0], list1[0][1]))
    

            


