find_unique_elements=list(input())
unique_elements = []
for num in find_unique_elements:
        if find_unique_elements.count(num) == 1:
            unique_elements.append(num)
            for x in unique_elements:
                print(x)
        else:
                print("False")

