a=eval(input())
count=[0]*26
for i in a:
    for j in i:
        count[ord(j)-97]+=1
for i in range(26):
    if count[i]>0:
        print(chr(i+97),count[i],sep=",")
