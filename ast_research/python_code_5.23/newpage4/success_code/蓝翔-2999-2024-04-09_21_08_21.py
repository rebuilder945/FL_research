juzi = input().split(' ')
a,b = input().split(' ')
c = int(a)
d = int(b)
juzi[c],juzi[d] = juzi[d],juzi[c]
print(juzi)
