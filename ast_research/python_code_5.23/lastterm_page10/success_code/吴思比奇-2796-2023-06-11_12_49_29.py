chara="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()"
s=list(input())
for i in s:
    if chara.find(i)!=-1:
        s[s.index(i)]='#'
snew=''.join(s)
sf=snew.split('#')
while '' in sf:
    sf.remove('')
if sf==[]:
    print('No digits')
else:
    a=0    
    for i in sf:
     if len(i)>=a:
       b=sf.index(i)
       a=len(i)
    print(sf[b])


