def  liebiaoqiantao(namelist,gradelist):
    q=[]
    for i in range(len(namelist)):
        q.append([namelist[i],int(gradelist[i])])
    return q
a=input().split (",")
b=input().split(",")
print(liebiaoqiantao(a,b))
