icard = input()
birthday = icard(6:10)+"-"+icard(10:12)+"-"+icard(12:14)
mask = icard(0:7)+"*"*8+icard(16:)
print(birthday)
print(mask)

