def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
   
    s = 0
    d = 0
    for i in range(a):
        d = d*10+a
        s += d
        print(d)


    print(s)
main()

