s_list = input().split()
n, m = map(int, input().split())
s_list[n], s_list[m] = s_list[m], s_list[n]
print(s_list)

