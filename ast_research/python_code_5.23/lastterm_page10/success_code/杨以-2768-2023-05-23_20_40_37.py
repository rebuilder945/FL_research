icard = input()
birthday = idcard[6:10]+"-"+idcard[10:12]+'-'+idcard[12:14]
mask = idcard[0:6]+'********'+idcard[14:]
print(birthday)
print(mask)

