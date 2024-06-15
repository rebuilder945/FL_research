ls=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
code1=input()
code2=''
for i in code1:
    if i.isalpha():
        if i.islower():
            for x in range(26):
                if i.upper()==ls[x]:
                    a=ls[26-x+1].lower()
                    code2=code2+a
        else:
            for x in range(26):
                if i==ls[x]:
                    a=ls[26-x+1].upper()
                    code2=code2+a
    else:
        code2=code2+i
print(code1)
print(code2)
