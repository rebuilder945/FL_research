def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    s = a
    for x in range(1,a):
        s += 10 ** a* x
    print(s)
       
main()

