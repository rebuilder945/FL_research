wordlist=eval(input())
a=0
for i in range(97,123):
    word=chr(i)
    for x in wordlist:
        b=x.count(word)
        a+=b
    a=0
    print(i,a)
   
