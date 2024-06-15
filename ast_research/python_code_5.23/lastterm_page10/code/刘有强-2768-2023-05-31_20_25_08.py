icard = input()
birthday = str(icard)[6:9]+"-"+str(icard)[10:11]+"-"+str(icard)[12:13]
mask = replace(str(icard)[6:13],"********"
print(birthday)
print(mask)

