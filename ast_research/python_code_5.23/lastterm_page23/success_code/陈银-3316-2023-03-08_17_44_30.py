male1 = int(input())
female1 = int(input())
sum1 = male1 + female1
mratio = male1 / sum1 * int(100)
fratio = female1 / sum1 * int(100)
a = "The male students ratio is %.2f%%,the female students ratio is %.2f%%" % (mratio,fratio)
print(a)
