icard = input()
birthday = ''.join(icard[7,11])
mask = icard.replace(icard[7,11],'********')
print(birthday)
print(mask)

