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
                lis1.append(s[i:i+max:1])
        else:
            break
if max == 0:
    print('No digitals')
else:
    print(lis1[-1])
                
            
