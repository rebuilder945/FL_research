male = eval(input())
female = eval(input())
total = male + female
# print('The male students ratio is %.2f%%,\
# the female students ratio is %.2f%%'%(male / total * 100, female / total * 100))
print('The male students ratio is {:.2f}%,\
the female students ratio is {:.2f}%'.format(male / total * 100, female / total * 100))
