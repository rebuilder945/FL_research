icard = input()
birthday = list(icard)[6:9]+"-"+list(icard)[10:11]+"-"+list(icard)[12:13]
mask = list(icard)[0:5]+"********"+list(icard)[-4:]
print(birthday)
print(mask)

