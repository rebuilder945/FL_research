wordlist=eval(input())
a=0
for i in range(chr(97),chr(123)):
    for x in wordlist:
        b=x.count(i)
        a+=b
    print(i,a)
    a=0
