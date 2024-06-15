icard = input()
birthday = int(icard[6,10]),'-',int(icard[10,12]),'-',int(icard[12,14])
mask = int(icard[0,6]),'********',int(icard[14,18])
print(birthday)
print(mask)

