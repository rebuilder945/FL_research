word = input()
fin = input()
x = len(fin)
list = []
s = [x for x in word]
i=0
for j in range(0,len(s)):
    i +=1
    if i<=len(word):
        if word[i-1:i-1+x:1] != fin:
            list.append(s[i])
        else:
            i+=x
print="".join(list)
