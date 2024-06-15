str1=input()
count_str={}
while (str1 !="q"):
    count_str.get(str1,0)+1
ls=[]
for k,v in count_str.items():
    ls.append([k,v])
ls.sort(key=lambda x:x[1],reverse=True)

print(ls[0][0]," ",ls[0][1])


