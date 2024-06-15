n = int(input())
original_list = list(range(1, n + 1))
shifted_list = original_list[1:] + [original_list[0]]
print(shifted_list)

