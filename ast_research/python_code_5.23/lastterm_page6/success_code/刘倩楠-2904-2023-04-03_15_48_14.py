def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    s = a
    for x in range(1,a*str):
        s += 10 ** x
    print(s)
       
main()

