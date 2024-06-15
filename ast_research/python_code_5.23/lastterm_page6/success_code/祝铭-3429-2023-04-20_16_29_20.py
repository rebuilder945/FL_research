s = input()
a = 0
b = 0
c = 0
d = 0
for x in str(s) :
    if x in ['q','w','e','r','t','y','u','i','o','p','l','k','j','h','g','f','d','s','a','x','z','c','v','b','n','m','A','Q','W','E','R','T','Y','U','I','O','P','D','S','F','G','H','J','K','L','Z','X','C','V','B','M','N'] :
        a += 1
    elif x in [' ']:
        b += 1
    elif x in ['0','1','2','3','4','5','6','7','8','9']:
        c += 1
    else :
        d += 1
print(a,b,c,d)
