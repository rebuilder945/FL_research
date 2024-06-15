lst=input().split()
stu={}
stu['englishi']='%.2f'%int(lst[1])
stu['python']='%.2f'%int(lst[2])
stu['math']='%.2f'%int(lst[3])
average=(int(lst[1])+int(lst[2])+int(lst[3]))/3
stulist=[]
for k,v in stu.items():
    stulist.append([k,v])
stulist.sort(key=lambda x:x[1],reverse=True)
print(lst[0],stulist[0][1],stulist[1][1],stulist[2][1],'%.2f'%average)
