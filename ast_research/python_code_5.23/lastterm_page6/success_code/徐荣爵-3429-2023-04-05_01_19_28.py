lst = list(input())
a = 0
b = 0
c = 0
d = 0
word = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','Z','V','W','X','Y')
num = ('1','2','3','4','5','6','7','8','9','0')
for i in lst:
    if i in word:
        a +=1
    elif i in num:
        c +=1
    elif i in [' ']:
        b +=1
    else:
        d +=1
print(a,b,c,d)

