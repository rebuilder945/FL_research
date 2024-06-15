def jisuan(boy,girl):
    persent1=boy/(boy+girl)*100
    persent2=girl/(boy+girl)*100
    return persent1,persent2
boy=eval(input())
girl=eval(input())
p1,p2=jisuan(boy,girl)
print("The male students ratio is %.2f%%,the female students ratio is %.2f%%"%(p1,p2))
