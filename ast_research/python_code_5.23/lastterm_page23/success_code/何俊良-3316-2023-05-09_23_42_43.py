male = int(input())
female = int(input())

total = male + female
male_ratio = male / total * 100
female_ratio = female / total * 100

print("The male students ratio is %.2f%%, the female students ratio is %.2f%%" % (male_ratio, female_ratio))
