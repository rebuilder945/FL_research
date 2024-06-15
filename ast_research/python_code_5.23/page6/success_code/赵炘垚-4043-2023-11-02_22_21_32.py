data = eval(input())
s = ' '.join(data)

counter = [0]*26

for c in s:
    counter[ord(c) - ord('a')] += 1

for i in range(len(counter)):
    if counter[i] != 0:
        print(f"{chr(ord('a') + i)},{counter[i]}")
