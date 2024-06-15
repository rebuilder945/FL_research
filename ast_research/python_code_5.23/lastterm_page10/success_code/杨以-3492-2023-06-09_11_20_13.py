s = input()
 
freq = {}
for c in s:
     if c in freq:
         freq[c] += 1
     else:
         freq[c] = 1
 
for c in s:
     if freq[c] == 1:
         print(c)
         exit()
 
print('None') 

