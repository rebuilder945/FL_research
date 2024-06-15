code=input()
codelist=list(code)
strong=0
if len(codelist)>=8:
    strong+=1

shuzi=['1','2','3','4','5','6','7','8','9','0']
counter3=0
for i in shuzi:
    if i in codelist:
        counter3+=1
if codelist!=0:
    strong+=1

zifu=['~','!','@','#','$','%','^','&','*','(',')','_','=','-','/',',','.','?','<','>',';',':','[',']','{','}','|']
counter=0
for i in zifu:
    if i in codelist:
        counter+=1
if counter!=0:
    strong+=1

xiaoxie=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
counter1=0
for i in xiaoxie:
    if i in codelist:
        counter1+=1
if counter1!=0:
    strong+=1

daxie=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
counter2=0
for i in daxie:
    if i in codelist:
        counter2+=1
if counter2!=0:
    strong+=1

print(strong)
