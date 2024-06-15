def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    list0 = []
    for i in range(a+1):
        m = str(a)*i
        list0.append(m)
    list0.pop(0)
    list0 = list(map(int,list0))
    print(sum(list0))
def jiuzheyangsuan(b):
    b = str(b)
    return b
main()

