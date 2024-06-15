icard = input()
birthday = str(icard)[6:10]+"-"+str(icard)[10:12]+"-"+str(icard)[12:14]
mask = icard.replace(str(icard)[6:13],"********")
print(birthday)
print(mask)

