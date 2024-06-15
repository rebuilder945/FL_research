icard = input()
birthday = ("{}-{}-{}".format(int(icard[8,12]),int(icard[12,14]),int(icard[14,16])))
mask = ("%d********%d"%(int(icard[0,6]),int(icard[-5:-1])))
print(birthday)
print(mask)

