icard = input()
birthday = icard[7:11]+'-'+icard[11:13]+'-'+icard[13:15]
mask = icard[:7]+'********'+icard[15:]
print(birthday)
print(mask)

