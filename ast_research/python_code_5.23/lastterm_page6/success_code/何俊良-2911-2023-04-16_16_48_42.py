def encrypt(data):
    encrypted = [(int(i) + 5) % 10 for i in data]
    n = len(encrypted)
    for i in range(n // 2):
        encrypted[i], encrypted[n - i - 1] = encrypted[n - i - 1], encrypted[i]
    return "".join(map(str, encrypted))
data = input()
print(encrypt(data))
