def find_unique_elements(lst):
    count = {}
    for num in lst:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    unique_elements = []
    for num, frequency in count.items():
        if frequency == 1:
            unique_elements.append(num)
    if unique_elements:
        unique_elements.sort()
        return ",".join(map(str, unique_elements))
    else:
        return False


list = input()
output= find_unique_elements(list)
print(output)  

