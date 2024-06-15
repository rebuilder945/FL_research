name=(input())
score=eval(input())
name1=[str(i) for i in name]
score1=[str(x) for x in score]
a=[[x+y for x in name1]for y in score1]
print(a)
