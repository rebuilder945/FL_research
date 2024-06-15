def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    list=[]
    for i in range(a):
        b=str(a)*(i+1)
        list.append(int(b))
    print(sum(list))
main()

