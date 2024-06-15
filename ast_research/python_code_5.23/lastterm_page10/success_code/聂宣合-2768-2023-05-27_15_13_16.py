icard = input()
birthday = icard[6:9]+"-"+icard[10:11]+"-"+icard[11:12]
mask = icard[6:13]+"********"+icard[-5:-1]
print(birthday)
print(mask)

