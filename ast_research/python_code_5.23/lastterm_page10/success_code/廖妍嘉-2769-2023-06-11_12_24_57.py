zimu=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
p=input()
n=list(p)
s=''
for i in n:
    if i.isalpha():
        if i.islower():
            for a in range(0,26):
                if i==zimu[a]:
                    r=zimu[25-a]
                    s+=r
        if i.isupper():
            for a in range(0,26):
                if i.lower()==zimu[a]:
                    r=zimu[25-a]
                    s+=r.upper()
    else:
        s+=i
print(p)
print(s)




