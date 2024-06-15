icard = input()
birthday = icard[6:10]+str('-')+icard[10:12]+str('-')+icard[12:14]
mask = icard[:6]+"*"*8+icard[14:]
print(birthday)
print(mask)

