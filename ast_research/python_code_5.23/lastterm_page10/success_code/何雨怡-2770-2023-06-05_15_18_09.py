word1=input()
word2=input()
word1list=word1.split()
word2list=word2.split()
if len(word1)==len(word2):
    if set(word1)==set(word2):
        print('True')
    else:
        print('False')
else:
    print("False")
