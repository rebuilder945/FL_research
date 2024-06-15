word1 = input()
word2 = input()

# 将字符串转换为列表，并按照字符排序
sorted_word1 = sorted(list(word1))
sorted_word2 = sorted(list(word2))

# 比较排序后的列表是否相等
if sorted_word1 == sorted_word2:
    print(True)
else:
    print(False)

