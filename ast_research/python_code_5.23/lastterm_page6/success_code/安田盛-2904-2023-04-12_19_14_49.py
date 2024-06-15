def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    s=a
    y=a
    for i in range(1,a):
        y=y*10+a
        s+=y
    print(s)
main()

