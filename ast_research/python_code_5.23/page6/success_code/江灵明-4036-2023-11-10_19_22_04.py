x = int(input())
if x in range(1,11):
    if x%2==0:
            print("black")
    else:
            print("red")
if x in range(11,19):
    if x%2==0:
            print("red")
    else:
            print("black")
if x in range(19,29):
    if x%2==0:
         print("black")
    else:
         print("red")
if x in range(29,37):
    if x%2==0:
        print("red")
    else:
            print("black")
if x == 0:
    print("green")
if x not in range(0,37):
    print("error")

    
