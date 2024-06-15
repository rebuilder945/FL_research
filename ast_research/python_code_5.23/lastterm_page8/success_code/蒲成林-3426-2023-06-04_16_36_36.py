# names = input().split(',')
# scores = list(map(int, input().split(',')))

# result = [[name, score] for name, score in zip(names, scores)]

# result.sort(key=lambda x: x[1])

# print(result)



x=float(input())
if x < 20:
    we=6*x**2+1
elif x>=20 and x<40:
    we=(3*x-60)**0.5
else:
    we=100/(x+1)
print('%.2f'%we)

