def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    s = 0
    num = a
    for i in range(a):
        s += num
        num = num*10 + a
    return s

main()

