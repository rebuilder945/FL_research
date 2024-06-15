string = input().split(' ')
place = eval(input()).split(' ')
strcopy = string[:]
string[place[0]] = strcopy[place[1]]
string[place[1]] = strcopy[place[0]]
print(string)
