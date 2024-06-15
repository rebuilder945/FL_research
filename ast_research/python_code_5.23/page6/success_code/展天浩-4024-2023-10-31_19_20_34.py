def main():
    a=int(input())
    calculate_sum(a)
def  calculate_sum(x):
    s=0
    for i in range(1,x+1):
        eva=0
        for j in range(1,j+1):
            eva=eva*(10**len(str(x)))+x
        s+=eva
    print(s)
main()

