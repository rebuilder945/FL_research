def decode(s):  
    """  
    将密码译回原文  
    """  
    s = list(s)  # 将字符串转换为列表，方便操作  
    n = len(s)  
    for i in range(n):  
        if s[i].isalpha():  
            if s[i].isupper():  
                s[i] = chr((ord('Z') - i + 1) % 26 + ord('A'))  
            else:  
                s[i] = chr((ord('z') - i + 1) % 26 + ord('a'))  
    return ''.join(s)  
  
if __name__ == '__main__':  
    password = input()  # 输入密码  
    print(password)  # 输出密码  
    text = decode(password)  # 将密码译回原文  
    print(text)  # 输出原文
