NaMe = input()
Points = eval(input())
ls = NaMe.split(',')
print(ls)
Points = [str(i) for i in Points]
f = [x+','+y for x in ls for y in Points]
print(f)
