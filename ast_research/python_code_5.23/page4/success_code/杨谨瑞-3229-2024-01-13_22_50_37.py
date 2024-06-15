str1 = input()
li1 = list(map(int, str1[1:-1].split(',')))
li2 = list(dict.fromkeys(li1))
if len(li2)==0:
    print('False')
else:
    for i in range(len(li2)):
        for j in range(len(li2)-i-1):
            if li2[j]>li2[j+1]:
                li2[j],li2[j+1]=li2[j+1],li2[j]
    for k in range(len(li2)):
        if k<len(li2)-1:
            print(li2[k],end=',')
        if k==len(li2)-1:
            print(li2[k])

