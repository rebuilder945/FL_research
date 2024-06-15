def partword(word1,word2):
    for i in range(len(word1)):
        w1=word1[:i+1]
        w2=word1[i+1:]
        w3=w2+w1
        if w3==word2:
            return True
        else:
            return False

word1=str(input())
word2=str(input())
print(partword(word1,word2))

