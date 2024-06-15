s=''
count={}
max_=0
while (s!='q'):
    s=input()
    count[s]=count.get(s,0)+1
    if count[s]>max_:
        max_=count[s]
for k,v in count.items():
    if v==max_:
        print(k,v)
