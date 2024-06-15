# l=eval(input())
# cuont=[0]*26
# for i in l:
    # for j in i:
    #    count[ord(j)-ord("a")] +=1




x = eval(input())
chars = [chr(i) for i in range(ord('a'),ord('z') + 1)]
count = [0] * 26
for i in x:
    for j in i:
        count[ord(j) - ord('a')] += 1
 
for c,cnt in zip(chars,count):
    if cnt > 0:
        print("%s,%d" %(c,cnt))    
        
    



