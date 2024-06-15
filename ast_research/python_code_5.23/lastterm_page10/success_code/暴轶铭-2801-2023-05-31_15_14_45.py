def check_number(password):
    for c in password:
        if c.isnumeric():
            return True
            break

def check_letter(password):
    for c in password:
        if 'a'<=c<='z' or 'A'<=c<='Z':
            return True
            break

def check_mark(password):
    for c in password:
        if not (c.isnumeric() or 'a'<=c<='z' or 'A'<=c<='Z'):
            return True
            break

def check_legal(password):
    if len(password)<8 or len(password)>16:
        print('长度需为8-16个字符,请重新输入。')
        return False
    else:
        for i in password:
            if 0x4e00<=ord(i)<=0x9fa5 or ord(i)==0x20: # Ox4e00等十六进制数分别为中文字符和空格的Unicode编码
                print('不能使用空格、中文，请重新输入。')
                return False
        else:
            key = 0
            key += 1 if check_number(password) else 0
            key += 1 if check_letter(password) else 0
            key += 1 if check_mark(password) else 0
            if key >= 2:
                return True
            else:
                print('至少含数字/字母/字符2种组合，请重新输入。')
                return False          

def main():
    while True:
        password = input('请输入密码：')
        if check_legal(password):
            strength_level = 0
            strength_level += 1 if check_number(password) else 0
            strength_level += 1 if check_letter(password) else 0
            strength_level += 1 if check_mark(password) else 0
            if strength_level == 2:
                print('密码设置成功！'+'*'*10+'强度等级中'+'*'*10)
                break
            else:
                print('密码设置成功！'+'*'*10+'强度等级高'+'*'*10)
                break
            
        else:
            continue

if __name__ == '__main__':
    main()

