code=input()
print(code)
a1=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lst=''
for i in code:
    if i.isalpha():  
            if i.isupper():
                for x in range(26):
                    if i==a1[x]:
                        i1=a1[26-x-1]
                        lst+=i1
            else :
                for x in range(26):
                    if i == a1[x].lower():
                        i2=a1[26-x-1].lower()
                        lst+=i2
    else:
        lst+=i
print(lst)
