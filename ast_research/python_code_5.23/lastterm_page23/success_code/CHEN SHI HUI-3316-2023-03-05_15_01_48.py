boy=eval(input())
girl=eval(input())

bn=boy/(boy+girl)
gn=girl/(boy+girl)

s="The male students ratio is %.2f%%,the female students ratio is %.2f%%"%(bn*100,gn*100)
print(s)
