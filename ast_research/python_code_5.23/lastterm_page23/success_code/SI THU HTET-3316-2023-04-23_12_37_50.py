male = int(input())  # 输入男生人数
female = int(input())  # 输入女生人数

total = male + female  # 总人数
male_ratio = round(male / total * 100, 2)  # 计算男生比例，保留两位小数
female_ratio = round(female / total * 100, 2)  # 计算女生比例，保留两位小数

# 输出结果
print("The male students ratio is {:.2f}%,the female students ratio is {:.2f}%".format(male_ratio, female_ratio))


