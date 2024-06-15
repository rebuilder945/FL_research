wordlist=eval(input())
word=[]
for i in range(97,123):
    word.append(chr(i))
for i in word:
    a=0
    for x in wordlist:
        if i in x:
            a+=x.count(i)
    if a!=0:
        print(i,a)
