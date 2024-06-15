icard = input()
birthday = ('%d-%d-%d'%(int(str(icard)[6:10]),int(str(icard)[10:12]),int(str(icard)[12:14])))
mask = icard.replace(str(icard)[6:14],'********')
print(birthday)
print(mask)

