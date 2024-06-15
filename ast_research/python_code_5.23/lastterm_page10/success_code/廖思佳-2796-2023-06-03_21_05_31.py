n=input()
s=""
max=""
for i in n:
    if i.isdigit():
        s=s+i
    else:
        if len(max)<=len(s):
            max=s
            
        s=""  
if s!="": 
    if len(max)<=len(s):
        max=s         
if len(max)==0:
    print("No digits")    
else:
    print(max)                
