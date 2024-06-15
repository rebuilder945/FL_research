def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    s = 0
    for x in range(a):
        b = str(a)
        x += 1
        b = b*x
        s += int(b)
    print(s)
main()

