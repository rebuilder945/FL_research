month=eval(input())
months=[[3,4,5],[6,7,8],[9,10,11],[12,1,2]]
seasons=['spring','summer','autumn','winter']
if month in range(1,13):
    for i in range(len(months)):
        if month in months[i]:
            print(seasons[i])
else:
    print('error')  
