my_list = list(input())
output = None
if not my_list:
    output = "None"
else:
    repeated_items = set([item for item in my_list if my_list.count(item) == 1])
    if repeated_items:
        output = repeated_items.pop()
print(output)
