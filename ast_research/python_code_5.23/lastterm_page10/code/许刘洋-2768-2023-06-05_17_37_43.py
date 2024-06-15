icard = input()
birthday = icard[6:10]+'-'+icard[10:12]+'-'+icard[12:14]
mask = icard.replaced(icard[6:14]),'*'*8)
print(birthday)
print(mask)

