def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    s = 0
    for x in range(a):
        s =s + eval(str(a) * (x+1))
    print(s)
main()

