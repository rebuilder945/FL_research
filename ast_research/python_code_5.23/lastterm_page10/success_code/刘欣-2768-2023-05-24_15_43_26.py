icard = input()
birthday = "{}-{}-{}".format(icard[7:11],icard[11:13],icard[13:15])
mask = "{}********{}".format(icard[:6],icard[15:])
print(birthday)
print(mask)

