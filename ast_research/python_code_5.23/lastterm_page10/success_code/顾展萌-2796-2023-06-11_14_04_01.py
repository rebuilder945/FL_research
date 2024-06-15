
def longest_digits_substring(s):
    max_len = 0
    start = -1
    end = -1

    # 遍历字符串s，记录当前数字子串的起始位置和终止位置
    cur_start = -1
    for i in range(len(s)):
        if s[i].isdigit():
            if cur_start == -1:
                cur_start = i
            cur_end = i

            # 更新最长数字子串的信息
            cur_len = cur_end - cur_start + 1
            if cur_len > max_len:
                max_len = cur_len
                start = cur_start
                end = cur_end
        else:
            cur_start = -1

    # 根据记录的起始位置和终止位置提取最长数字子串
    if start != -1 and end != -1:
        return s[start:end+1]
    else:
        return "No digits"

s = input().strip()
print(longest_digits_substring(s))

