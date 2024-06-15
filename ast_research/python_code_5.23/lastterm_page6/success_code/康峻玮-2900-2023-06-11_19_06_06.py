def is_prime(num):
    if num < 2:         # 1不是质数，小于1的数也不是质数
        return False
    for i in range(2, int(num**0.5)+1):   # 只需要判断到num的平方根即可
        if num % i == 0:
            return False
    return True

def is_palindrome(num):
    str_num = str(num)
    return str_num == str_num[::-1]     # 使用字符串翻转判断是否回文

def find_palindrome_primes(n):
    if n <= 1 or type(n) != int:        # 检查n是否合法
        print('illegal input')
        return
    primes = []
    for i in range(2, n+1):
        if is_prime(i) and is_palindrome(i):
            primes.append(str(i))
    print(' '.join(primes))

def main():
    n = eval(input())
    find_palindrome_primes(n)

if __name__ == '__main__':
    main()
