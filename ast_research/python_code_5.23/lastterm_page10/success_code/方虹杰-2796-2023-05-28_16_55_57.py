
def find(s):
    max = 0
    count = 0
    end = 0
    for i in range(len(s)):
        if (s[i] >= '0' and s[i] <= '9'):
            count+=1
            if (max < count):
                max = count
                end = i
        else:
            count = 0
    print(s[end - max + 1:end + 1])
if __name__ == "__main__":
    s = str(input())
    find(s)


