list = [str(x) for x in range(0,10)]
lis1 = []
s =  input()
word = [x for x in s]
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
        c = 0
        for j in range(i,len(word)):
            if word[j] in list:
                c+=1
            else:
                if c == max:
                    lis1.append(s[i-1:i+max-1:1])
    print(lis1[-1])
            
