from collections import Counter
def strcount(s):
    c=Counter(s.split())
    most_common=c.most_common()
    max_count=most_common[0][1]
    print("出现次数最多的单词：")
    for word,count in most_common:
        if count==max_count:
            print(f"{word}出现次数:{count}")





