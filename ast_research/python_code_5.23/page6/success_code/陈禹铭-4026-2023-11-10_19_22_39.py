n=eval(input())
numerator=2
denomination=1
sum_fraction=0.0
for _ in range(n):
    sum_fraction+=numerator/denomination
    numerator,denomination=numerator+denomination,numerator
print(sum_fraction)
