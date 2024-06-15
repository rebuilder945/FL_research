icard = input()
birthday = icard[6:14]
mask = icard[0:6]+str("********")+icard[14:]
print(birthday)
print(mask)

