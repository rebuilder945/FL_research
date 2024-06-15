def  liebiaoqiantao(namelist,gradelist):
    q=[]
    for i in range(len(namelist)):
        q.append([namelist[i],int(gradelist[i])])
    q.sort(key=lambda x:x[1],reverse=False)
    return q
a=input().split (",")
b=input().split(",")
print(liebiaoqiantao(a,b))
