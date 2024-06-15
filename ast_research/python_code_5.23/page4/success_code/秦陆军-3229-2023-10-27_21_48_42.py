#【问题描述】
#输入一个自然数列表，找出只出现一次的元素，并升序输出。如果没有只出现一次的元素，则输出False。
#【输入形式】
#输入包含自然数的列表，包括方括号，逗号分隔
#排序后的数字，每个数字之间用英文逗号分隔。或者False。
#【样例输入1】
#[1,2,3,5,2,3,4]
#【样例输出1】
#1,4,5
#【样例输入2】
#[9,9,9,12,12]
#【样例输出2】
#False
#【样例说明】
#[9,9,9,12,12]列表中，9出现3次，12出现2次，没有出现一次的元素，则输出False。
#【评分标准】
lst1 = input()
if lst1:
    lst1 = eval(lst1)
    lst2 = []
    for x in lst1:
        if lst1.count(x) == 1 and x not in lst2:
            lst2.append(x)
    if not lst2:
        print("False")
    else:
        lst2.sort()
        result = ','.join(map(str, lst2))
        print(result)
else:
    print("False")

      
