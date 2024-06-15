icard = input()
birthday = idcard[6:9]+"-"+idcard[10:11]+"-"+idcard[12:13]
mask = idcard.replace(idcard[6:13],"********")
print(birthday)
print(mask)

