objs = [x for x in input().strip('[]').split(',')]
 
for obj in objs:
     if not isinstance(obj, str):
         print('Input contains non-string objects!')
         exit()
 
freq = {}  
for s in objs:
     for c in s:
         if c.islower():   
             if c in freq:
                 freq[c] += 1
             else:
                 freq[c] = 1  
 
chars = sorted(freq.keys())
for c in chars:
     print(c + ',' + str(freq[c])) 

