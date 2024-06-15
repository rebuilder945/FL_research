ls=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
s=input()
ss=''
for i in s:    
    if i.isalpha():        
        if i.islower():            
            for x in range(26):                
                if i.upper()==ls[x]:                    
                    a=ls[26-x-1].lower()                    
                    ss+=a        
        else:            
            for x in range(26):                
                if i==ls[x]:                    
                    a=ls[26-x-1]                    
                    ss+=a    
    else:        
        ss+=i
print(s)
print(ss)
