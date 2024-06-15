def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
        list=[a]
        for i in range(1,a):
                word=str(a)
                for i in range(0,i):
                        word=int(str(word)+str(a))
                list.append(int(word))
        print(sum(list))
main()

