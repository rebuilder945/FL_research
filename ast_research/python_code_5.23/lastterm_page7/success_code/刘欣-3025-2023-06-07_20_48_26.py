lis=input().split()
dic={}
for i in lis:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
lis1=list(dic.items())
lis1.sort(key=lambda x:-x[1])
for i in range(len(lis1)):
    if lis1[i][1]==lis1[0][1]:
        print(f"{lis1[i][0]} {lis1[i][1]}\n")
