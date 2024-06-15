a=input("")
num=[]
while a!='q':
    num.append(a)
    a=input("")
b=[(a,num.count(a)) for a in num]
s=[num.count(a) for a in num]
dic=dict(b)
for x in dic.keys():
    if  dic[x]==max(s):
        print(x,max(s))

    




