icard = input()
birthday = "%s-%s-%s"%(icard[6:10],icard[10:12],icard[12:14])
mask = "%s********%s"%(icard[0:6],icard[14:])
print(birthday)
print(mask)

