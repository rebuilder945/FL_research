find_unique_elements=eval(input())
unique_elements = []
for num in find_unique_elements:
        if find_unique_elements.count(num) == 1:
            unique_elements.append(num)
            print(unique_elements)
else:
        print("Fales")

