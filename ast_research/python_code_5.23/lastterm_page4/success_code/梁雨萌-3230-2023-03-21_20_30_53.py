lis=eval(input())
lis.sort()
lis.reverse()
word=str(lis[0])
for i in range(1,len(lis)):
    word=word+str(lis[i])
print(word)
    
