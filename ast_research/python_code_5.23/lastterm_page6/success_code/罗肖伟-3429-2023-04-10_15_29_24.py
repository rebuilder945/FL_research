a2=input()
lst=[]
for i1 in range(len(a2)):
    lst.append(a2[i1])
a1=0
b1=0
c1=0
for x1 in lst:
    if x1 in ['a','b','c','d','e','f','h','i','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',]:
        a1+=1
    elif x1 in[' ']:
        b1+=1
    elif x1 in ['0','1','2','3','4','5','6','7','8','9']:
        c1+=1
d1=len(a2)-a1-b1-c1
print(a1,b1,c1,d1)        
        
