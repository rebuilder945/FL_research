sname=input().split(',')
sdate=input().split(',')
for i in range(len(sname)):
    s=[]
    s.append(sname[i])
    s.append(eval(sdate[i]))
    print(s)
