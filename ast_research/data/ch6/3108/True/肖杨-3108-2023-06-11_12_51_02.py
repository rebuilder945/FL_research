a=eval(input())
b=[0]*26
for i in a:
    for j in i:
        b[ord(j)-ord('a')]+=1
for i in range(26):
    if b[i]>0:
        print(chr(i+ord('a')),b[i],sep=',')

