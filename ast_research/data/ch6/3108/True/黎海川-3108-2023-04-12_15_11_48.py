a=list(eval(input()))
count=[0]*26
for i in a:
    for j in i:
        count[ord(j)-ord("a")]=count[ord(j)-ord("a")]+1
for i in range(0,26):
    if count[i]>0:
        print(chr(ord("a")+i),count[i],sep=',')

