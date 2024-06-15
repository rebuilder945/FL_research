str1 = input()
li1 = list(map(int, str1[1:-1].split(',')))
li2 = list(dict.fromkeys(li1))
for i in range(len(li2)):
    for j in range(len(li2)-i-1):
        if li2[j]>li2[j+1]:
            li2[j],li2[j+1]=li2[j+1],li2[j]
for l in range(len(li2)-1,-1,-1):
    counter=0
    for m in range(len(li1)):
        if li2[l]==li1[m]:
            counter+=1
        if counter==2:
            del li2[l]
            break
if len(li2)==0:
    print('False')        
for k in range(len(li2)):
    if k<len(li2)-1:
        print(li2[k],end=',')
    if k==len(li2)-1:
        print(li2[k])

