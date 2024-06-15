icard = input()
birthday = ("%d-%d-%d"%(int(icard[6:10]),int(icard[10:12]),int(icard[12:14])))
mask = ("%d********%d"%(int(icard[0:6]),eval(icard[-4:-1])))
print(birthday)
print(mask)

