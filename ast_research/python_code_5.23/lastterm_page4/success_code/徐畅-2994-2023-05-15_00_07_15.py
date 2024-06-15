lat=list(map(int,input().split(',')))
n,m=map(int,input().split(','))
if n < len(lat):

    lst=[]
    lst.append(lat[n])
    lst=lst*m
    lat=lat+lst
    print(lat)
else:
    print("error")
