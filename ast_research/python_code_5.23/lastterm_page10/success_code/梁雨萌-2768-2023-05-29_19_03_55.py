icard = input()
birthday = str(icard[6:10:1])+'-'+str(icard[10:12:1])+'-'+str(icard[12:14:1])
mask = str(icard[0:6:1])+"********"+str(icard[14:18:1]) 
print(birthday)
print(mask)

