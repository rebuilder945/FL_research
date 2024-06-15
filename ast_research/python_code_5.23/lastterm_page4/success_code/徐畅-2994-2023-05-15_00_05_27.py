lat=list(map(int,input().split(',')))
n,m=map(int,input().split(','))
if n in range(len(lat)+1):

    lst=[]
    lst.append(lat[n])
    lst=lst*m
    lat=lat+lst
    print(lat)
else:
    print("error")
