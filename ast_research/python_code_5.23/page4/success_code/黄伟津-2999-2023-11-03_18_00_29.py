lst = input()
s = input()
lst = lst.split(" ")
s = s.split(" ")
n = int(s[0])
m = int(s[1])
lst[n] , lst[m] = lst[m] , lst[n]
print(lst)

