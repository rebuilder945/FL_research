word=eval(input())
a=str(word[0])
for i in range(1,len(word)):
        a=a+" "+str(word[i])
lis=list(a)
lis.sort()
count1=[]
count2=[]
for i in lis:
    if i not in count1:
        lis.append(i)
        a=lis.count(i)
        count2.append(a)
    else:
        a=lis.index(i)
        count2[a]=count2[a]+lis.count(i)
for i in range(0,len(count1)):
    print(count1[i],",",count2[i])
        
