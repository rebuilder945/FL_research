strs = [x for x in input().strip('[]').split(',')]
 
freq = {}
for s in strs:
     for c in s:
         if c in freq:
             freq[c] += 1
         else:
             freq[c] = 1
 
for c in sorted(freq):
     print(c + ',' + str(freq[c]))
