string = input().split(' ')
place = input().split(' ')
strcopy = string[:]
string[int(place[0])] = strcopy[int(place[1])]
string[int(place[1])] = strcopy[int(place[0])]
print(string)
