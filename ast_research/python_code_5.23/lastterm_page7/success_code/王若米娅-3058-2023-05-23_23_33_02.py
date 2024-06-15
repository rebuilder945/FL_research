str1=input() or "q"
count_str={}
while (str1 !="q"):
    str2=input()
    count_str.get(str2,0)+1
ls=[]
for k,v in count_str.items():
    ls.append([k,v])

print(ls[0][1])


