strings = input().split()
n, m = map(int, input().split())
strings[n], strings[m] = strings[m], strings[n]
print(strings)

