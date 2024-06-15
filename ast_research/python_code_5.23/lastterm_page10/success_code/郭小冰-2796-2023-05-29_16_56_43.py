import re
def find(s):
    max = 0
    count = 0
    end = 0
    if bool(re.search(r'\d', s))==False:
        print('No')
    else:
        for i in range(len(s)):
            if (s[i] >= '0' and s[i] <= '9'):
                count += 1
                if (max < count):
                    max = count
                    end = i
            else:
                count = 0
        print(s[end - max + 1:end + 1])

s = str(input())
find(s)

