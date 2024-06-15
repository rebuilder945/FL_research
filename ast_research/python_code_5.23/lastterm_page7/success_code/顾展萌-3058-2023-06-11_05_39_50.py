word_dict = {}
while True:
    s = input()
    if s == 'q':
        break
    if s in word_dict:
        word_dict[s] += 1
    else:
        word_dict[s] = 1
 
result_elem = max(word_dict.items(), key=lambda item: item[1])
print("%s %d" % (result_elem[0], result_elem[1]))













