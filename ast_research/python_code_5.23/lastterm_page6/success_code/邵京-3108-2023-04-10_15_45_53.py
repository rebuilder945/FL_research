wordlist=eval(input())
a=0
for i in range(97,123):
    word=chr(i)
    for x in wordlist:
        if word in x:
            b=x.count(word)
            a+=b
        else:
            break
    print(chr(i),',',a)
    a=0
   
