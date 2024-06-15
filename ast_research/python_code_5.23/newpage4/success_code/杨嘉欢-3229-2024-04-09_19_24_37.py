def unique_element(numbers):
    counts={}
    for num in numbers:
        if num in counts:
            counts[num]+=1
        else :
            counts[num]=1
        unique_elements = [num for num, count in counts.items() if count == 1]
    if unique_elements:
        sorted_elements=sorted(unique_elements)
        sorted_elements=[str(element)for element in sorted_elements]
        sorted_elements = ",".join(sorted_elements)
        return sorted_elements
    else:
        return False
input=input()
numbers=input[1:-1]
numbers = list(map(int, numbers.split(",")))
result = unique_element(numbers)
if result:
    print(result)
else:
    print("False")

