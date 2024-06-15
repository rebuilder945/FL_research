icard = input()
birthday = ("%d-%d-%d"%(icard[8:12],icard[12:14],icard[14:16]))
mask = ("%d********%d"%(icard[0:6],icard[-5:-1]))
print(birthday)
print(mask)

