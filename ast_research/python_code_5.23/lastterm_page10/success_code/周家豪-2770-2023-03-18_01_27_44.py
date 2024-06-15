str1=input()
str2=input()
i=0
for x in str1:
    if str1.count(x)!=str2.count(x):
        i+=1
print (True if i==0 else False)
