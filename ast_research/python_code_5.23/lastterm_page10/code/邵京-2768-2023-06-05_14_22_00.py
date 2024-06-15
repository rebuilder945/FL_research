icard = input()
birthday = icard[6:10]+'-'+icard[10:12]+'-'+icard[12:14]
mask = icard.replace(icard[i] for i in range (6,15),'*')
print(birthday)
print(mask)

