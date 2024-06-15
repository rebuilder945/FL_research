male_num = int(input("请输入男生人数："))
female_num = int(input("请输入女生人数："))
total = male_num + female_num
male_ratio = male_num / total * 100
female_ratio = female_num / total * 100
print("The male students ratio is {:.2f}%,the female students ratio is {:.2f}%".format(male_ratio, female_ratio))

