juzi = input().split(' ')
a,b = eval(input())
juzi[a],juzi[b] = juzi[b],juzi[a]
print(juzi)
