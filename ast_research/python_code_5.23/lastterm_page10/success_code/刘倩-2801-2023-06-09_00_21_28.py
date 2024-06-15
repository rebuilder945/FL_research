mima = input()
jibie = [0,0,0,0,0]
teshu = "~!@#$%^&*()_=-/,.?<>;:[\]{\}|\\"


for x in mima :
    if x.isdigit():
        jibie[0] = 1
    if x.islower():
        jibie[1] = 1
    if x.isupper():
        jibie[2] = 1
    if len(mima) > 8:
        jibie[3] = 1
    if x in teshu:
        jibie[4] = 1

    print(jibie.count(1))




