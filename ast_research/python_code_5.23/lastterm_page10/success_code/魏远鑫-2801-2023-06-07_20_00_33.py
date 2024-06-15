start=0
n=input()
if len(n)>=8:
    start+=1
for i in n:
    if i.islower():
        start+=1
        break
for i in n:    
    if i.isupper():
        start+=1
        break
for i in n:   
    if i.isdigit():
        start+=1
        break
for i in n:    
    if i in "~!@#$%^&*()_=-/,.?<>;:[]{}|":
        start+=1
        break
print(start)
               
