lst = []
result = sorted(set(lst), key=lambda i: lst[::-1].index(i), reverse=True)
print(result)
