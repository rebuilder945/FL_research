s=input()
count={}
max=0
count[s]=count.get(s,0)+1
if count[s]>max:
    max=count[s]
for k,v in count.items():
    if(v==max):
        print(k)
