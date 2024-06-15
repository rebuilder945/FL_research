list = [str(x) for x in range(0,10)]
lis1 = []
s =  input()
word = s.split()
max = 0
for i in range(0,len(word)):
    count = 0
    for j in range(i,len(word)):
        if word[j] in list:
            count+=1
            if count >= max:
                max = count
        else:
            break
                
if max == 0:
    print('No digits')
else:
    for i in range(0,len(word)):
        count = 0
        for j in range(i,len(word)):
            if word[j] in list:
                count+=1
            if count == max:
                lis1.append(s[i:i+1+count:1])
    print(lis1[-1])
            
