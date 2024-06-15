def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(b):
    jishu=0
    for i in range(1,b+1):
        m=0
        for j in range(1,i+1):
            m=m*(10**len(str(b)))+b
        jishu+=n
    print(jishu)
main()

