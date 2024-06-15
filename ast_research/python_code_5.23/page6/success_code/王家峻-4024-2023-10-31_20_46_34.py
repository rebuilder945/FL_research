def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    t=0
    for i in range(1,a+1):
        eva=0
        for j in range(1,i+1):
            eva=eva*(10**len(str(x)))+x
            t+=eva
    print(t)
main()

