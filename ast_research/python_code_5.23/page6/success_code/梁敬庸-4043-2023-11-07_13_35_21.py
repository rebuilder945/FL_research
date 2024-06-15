a=eval(input())
counts = [0] * 26
for i in a:
    for j in i:
        counts[ord(j)-ord('a')]+=1
for i in range(26):
    if counts[i]>0:
        print(chr(ord('a')+i),counts[i],sep=',')

