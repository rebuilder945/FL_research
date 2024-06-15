lis=eval(input())
lis.sort()
lis.reverse()
word=str(lis[0])
for i in range(1,len(lis)):
    if max(lis)!=0:
        word=word+str(lis[i])
    else:
        word=0
print(word)
    
