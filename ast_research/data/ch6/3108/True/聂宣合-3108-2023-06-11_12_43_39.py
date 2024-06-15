def count_letters(lst):
    counts = {}
    for word in lst:
        for letter in word:
            if letter in counts:
                counts[letter] += 1
            else:
                counts[letter] = 1
    for letter in sorted(counts):
        print(f'{letter},{counts[letter]}')

lst = eval(input())
count_letters(lst)

