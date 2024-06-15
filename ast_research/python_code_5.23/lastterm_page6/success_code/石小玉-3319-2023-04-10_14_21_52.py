mathScores = int(input())
languageScores = int(input())

if mathScores >= 99 and languageScores >= 99:
    print("You won a scholarship of 500 yuan!")
elif mathScores <= 30 and languageScores <= 30:
    print("You need to relearn!")
