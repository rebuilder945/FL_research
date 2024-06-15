a=input()
b=0
c=list(a)
if len(a)>=8:
    b=b+1
for x in range(len(c)):
    if c[x] in  ['1','2','3','4','5','6','7','8','9','0']:
        b=b+1
        break
for x in range(len(c)):
    if c[x] in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']:
        b+=1
        break
for x in range(len(c)):
    if c[x] in ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']:
        b+=1
        break
for x in range(len(c)):
    if c[x] in ['~','!','@','#','$','%','^','&','*','(',')','_','=','-','/',',','.','?','<','>',';',':','[',']','{','}','|','\\']:
        b+=1
        break    
print(b)
