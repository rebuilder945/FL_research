student = eval(input())
info = (student[1],student[2])
avg = sum(student[6])
#出现报错 list index out of range 的原因可能是：
#用户输入的列表长度不够长，导致你尝试访问超出列表长度的索引。
#用户输入的内容不符合预期，无法正确解析成列表，导致后续索引操作失败。
print(info)
print("%.2f"%avg)

