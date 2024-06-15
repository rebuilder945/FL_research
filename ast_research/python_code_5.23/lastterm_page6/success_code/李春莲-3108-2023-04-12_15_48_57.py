lst=eval(input())
char1=[chr(x) for x in range(ord('a'),ord('z')+1)]      
count=[0]*26      
for x in lst:    
    for c in x:     
        count[ord(c)-ord('a')]+=1   
for c,cnt in zip(char1,count):       
    if cnt>0:
        print('%s,%d'%(c,cnt))

