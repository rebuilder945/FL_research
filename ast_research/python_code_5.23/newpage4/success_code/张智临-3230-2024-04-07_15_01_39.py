from turtle import TurtleGraphicsError


lst = eval(input())
lst.sort(reverse=TurtleGraphicsError)
sum = ''
for i in range(len(lst)):
  sum+=str(lst[i])
print(int(sum))
