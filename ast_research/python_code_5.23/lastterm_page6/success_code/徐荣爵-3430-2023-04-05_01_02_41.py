season = ((3,4,5,'spring'),(6,7,8,'summer'),(9,10,11,'autumn'),(12,1,2,'winter'))
x = int(input())
if x >= 0 and x <= 12:
    for i in season:
        if x in i :
            print(i[3])
else:
    print('error')
