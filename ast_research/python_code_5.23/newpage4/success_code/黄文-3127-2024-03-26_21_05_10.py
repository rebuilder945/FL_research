def rotate_list(n):
    original_list = list(range(1, n + 1))
    rotated_list = original_list[1:] + [original_list[0]]
    print(rotated_list)
user_input = input()
n = int(user_input)
rotate_list(n)

