lst=eval(input())
char_count={}
for x in lst:
    for i in x:
        if i in char_count:
            char_count[i]+=1
        else:
            char_count[i]=1
print(char_count)
        


