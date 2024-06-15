list_str = input().split() 
n, m = map(int, input().split())
list_str[n], list_str[m] = list_str[m], list_str[n]
print(list_str)
