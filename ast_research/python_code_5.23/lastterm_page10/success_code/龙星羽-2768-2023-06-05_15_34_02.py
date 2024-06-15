icard = input()
birthday = icard[6:15]
mask = icard[:6]+"*"*8+icard[15:]
print(birthday)
print(mask)

