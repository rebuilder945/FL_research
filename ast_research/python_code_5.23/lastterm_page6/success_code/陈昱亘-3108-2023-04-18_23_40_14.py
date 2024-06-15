lst=eval(input())
string=''.join(lst)
n=0
for i in range(26):
    for x in string:
        if x==chr(ord('a')+i):
            n+=1
    if n>0:
        print('{},{}'.format(chr(ord('a')+i),n))
        n=0
    else: continue
