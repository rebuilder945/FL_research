name=eval(input())
grade=eval(input())
new= [[name, score] for name, score in zip(name, grade)]
print(new)
