str1=input()
str2={}
while str1 != 'q':
    str2[str1]=str2.get(str1,0)+1
max_count=0
for key in str2:
    if str2[key]>max_count:
        max_count=str2[key]
        max_key=key
print(max_key,max_count)
