icard = input()
birthday = icard[6:11]+'-'+icard[11:13]+'-'+icard[13:15]
mask = icard[0:6]+'********'+icard[15:20]
print(birthday)
print(mask)

