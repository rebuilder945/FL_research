word = input()
dig = '0123456789'
up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
low = 'abcdefjhijklmnopqrstuvwxyz'
sym = '~!@#$%^&*()_=-/,.?<>;:[]|\}{'
count = 0
dic ={count:0,dig:0,up:0,low:0,sym:0}
if len(word)>=8:
    dic[count]=1
for i in word:
    if i in dig:
        dic[dig]=1
    if i in up:
        dic[up]=1
    if i in low:
        dic[low]=1
    if i in sym:
        dic[sym]=1
all = dic.values()
sum = 0
for i in all:
    sum +=i
print(sum)

