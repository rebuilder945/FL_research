icard = input()
birthday = "_".join(icard(6,10),idcard(10,12),idcard(12,14))
mask = icard.replace(idcard(6,14),"*")
print(birthday)
print(mask)

