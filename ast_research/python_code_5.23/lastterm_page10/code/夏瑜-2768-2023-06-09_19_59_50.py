icard = input()
birthday = icard[7:15]
mask = icard[0:7]+str(********)+icard[15:]
print(birthday)
print(mask)

