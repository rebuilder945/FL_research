name=eval(input())
score=eval(input())
score1=[str(x) for x in score]
a=[[x+y for x in name]for y in score1]
print(a)
