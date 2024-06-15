male = int(input())
female = int(input())
total = male+female
rm = "%.2f"%((male/total)*100)
rf = "%.2f"%((female/total)*100)
s1 ="%,the female students ratio is"
print("The male students ratio is",rm+(s1.rstrip()),rf+"%")
