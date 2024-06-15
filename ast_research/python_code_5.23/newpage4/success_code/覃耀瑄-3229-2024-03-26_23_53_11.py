def find_unique_elements(nums):
    unique_elements = []
    for num in nums:
        if nums.count(num) == 1:
            unique_elements.append(num)
            print(unique_elements)
    else:
        print("Fales")

