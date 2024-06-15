def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    for i in range(a):
        s = s + int(str(a)*(i+1))
    print(s)
main()

