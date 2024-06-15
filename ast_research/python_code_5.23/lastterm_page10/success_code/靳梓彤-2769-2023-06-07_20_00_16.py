code=input()
print(code)
a1=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lst=''
for i in code:
    if i.isalpha():  
            if i.isupper():
                for x in range(26):
                    if i==a1[x]:
                        i=a1[x].lower()
                        lst+=i
            else :
                for x in range(26):
                    if i == a1[x].lower():
                        i=a1[x].upper()
                        lst+=i
    else:
        lst+=i
print(lst)
