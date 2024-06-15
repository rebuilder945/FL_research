dic={}
while True:
        i=input()
        if i=='q':
            break
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1
maxnum=max(dic.values())
for str,num in dic.items():
     if num==maxnum:
          print(str,num)

