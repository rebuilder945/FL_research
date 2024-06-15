x=input()
english_count=0
kongge_count=0
number_count=0
qita_count=0
for i in x:
    if 'a'<=i<='z' or 'A'<=i<='Z':
        english_count+=1
    elif i==' ':
        kongge_count+=1
    elif '0'<=i<='9':
        number_count+=1
    else:
        qita_count+=1
print("%d %d %d %d"%(english_count,kongge_count,number_count,qita_count))


