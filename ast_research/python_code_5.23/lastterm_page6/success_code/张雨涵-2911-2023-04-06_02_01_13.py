d = list(str(input()))
s=[]
for i in range(len(d)):
    t = (int(d[i])+5)%10
    s.insert(0,t)
    str="".join('%s' %id for id in s)
print(str)
#转列表为字符串
