icard = input()
birthday = '%d-%d-%d'%(icard[7,11],icard[11,13],icard[13,15])
mask = icard.replace(icard[7,16],'*')
print(birthday)
print(mask)

