n=input() or 'q'
dic={}
while n != 'q':
    if n not in dic:
        dic[n]=1
    else:
        dic[n]+=1
    n=input() or 'q'
max=max(dic.values())
for r,num in dic.items():
    if num==max:
        print(r,num)

