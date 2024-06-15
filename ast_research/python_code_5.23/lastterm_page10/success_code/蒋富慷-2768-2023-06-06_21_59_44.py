icard = input()
birthday = icard[6,14]
mask = icard.replace(birthday,'********')
print(birthday)
print(mask)

