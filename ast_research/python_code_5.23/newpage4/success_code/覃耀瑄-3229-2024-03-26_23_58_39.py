find_unique_elements=list(input())
unique_elements = []
for num in find_unique_elements:
        if find_unique_elements.count(num) == 1:
            unique_elements.append(num)
            n=int(unique_elements)
            print(n)
        else:
                print("False")

