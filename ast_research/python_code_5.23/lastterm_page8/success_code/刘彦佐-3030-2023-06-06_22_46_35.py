def  liebiaoqiantao(namelist,gradelist):
    q=[]
    for i in range(len(namelist)):
        q.append([namelist[i],gradelist[i]])
    return q
a=input().split (",")
b=input().split(",")
liebiaoqiantao(a,b)
