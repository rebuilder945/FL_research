icard = input()
birthday = icard[6:10]+'-'+icard[10:12]+'-'+icard[12:14]
mask = icard.replace('{}'.format(birthday.strip('-')),'********')
print(birthday)
print(mask)

