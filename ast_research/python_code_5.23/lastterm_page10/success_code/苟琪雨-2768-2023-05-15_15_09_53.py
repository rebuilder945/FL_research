icard = input()
birthday = range(icard[7:11])+"-"+range(icard[11:13])+"-"+range(icard[13:15])
mask = range(icard[0:6])+"*"*8+range(icard[-4:-1])
print(birthday)
print(mask)

