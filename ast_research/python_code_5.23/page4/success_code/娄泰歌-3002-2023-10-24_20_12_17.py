def calculate_average(lst):  
    if len(lst) == 0:  
        return None  
    else:  
        return sum(lst) / len(lst)  
  
lst = [int(i) for i in input("请输入一个整数列表，包含方括号，列表元素用逗号分隔：").strip()]  
avg = calculate_average(lst)  
if avg is None:  
    print("列表为空")  
else:  
    if round(avg, 2) == avg:  
        print(int(avg))  
    else:  
        print("{:.2f}".format(avg))
