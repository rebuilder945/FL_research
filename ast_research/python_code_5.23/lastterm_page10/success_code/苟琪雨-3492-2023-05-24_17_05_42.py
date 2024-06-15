str=input()
lst=[]
flag=0
for i in str:
    if str.count(i)==1:
        lst.append(i)
        flag+=1
if flag>0:
    print(lst[0])
else:
    print("None")
