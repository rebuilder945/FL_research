# n=input().split(",")
# s=input().split(",")
# a=[x+','+y for x in n for y in s]
# print([a])

names = input().split(",")
scores_str = input()
scores = [int(s) for s in scores_str[1:-1].split(",")]
result = [[names[i], scores[i]] for i in range(len(names))]
print(result)

