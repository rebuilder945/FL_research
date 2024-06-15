icard = input()
birthday = f"{id_card[6:10]}-{id_card[10:12]}-{id_card[12:14]}"
mask = id_card[:6] + "********" + id_card[-4:]
print(birthday)
print(mask)

