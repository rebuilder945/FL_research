num=eval(input())
month=[[3,4,5],[6,7,8],[9,10,11],[12,1,2]]
season=["spring","summer","autumn","winter"]
flag=0
for i in range(len(month)):
    if num in month[i]:
        print(season[i])
        flag=1
        break
if flag == 0:
    print("error")

