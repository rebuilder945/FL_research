icard = input()
birthday = str(icard[6:10]-icard[10:12]-icard[12:14])
mask = str(icard[0:6])+str(*)*8+str(icard[14:18])
print(birthday)
print(mask)

