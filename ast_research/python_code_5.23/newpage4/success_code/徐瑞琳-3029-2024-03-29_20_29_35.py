NaMe = input()
Points = eval(input())
ls = NaMe.split('')
fin = [[x+','+y for x in ls for y in Points]]
print(fin)
