from collections import Counter  
  
def find_single_numbers(lst):  
    count = Counter(lst)  
    single_numbers = [num for num, count in count.items() if count == 1]  
    if single_numbers:  
        return ','.join(map(str, single_numbers))  
    else:  
        return False  
  
# 测试样例  
print(find_single_numbers([1,2,3,5,2,3,4]))  # 输出：1,4,5  
print(find_single_numbers([9,9,9,12,12]))  # 输出：False
