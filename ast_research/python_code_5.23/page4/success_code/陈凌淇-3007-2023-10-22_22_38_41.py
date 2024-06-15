input_list = input()
n, m = map(int, input().split(','))

# Convert input_list to a list
lst = eval(input_list)

# Check if n and m are within the list bounds
if 0 <= n <= m < len(lst):
    # Delete elements from n to m (excluding m)
    del lst[n:m]

    # Output the result
    print(lst)
else:
    print("error")
