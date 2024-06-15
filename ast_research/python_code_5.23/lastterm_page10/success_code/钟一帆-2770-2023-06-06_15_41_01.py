w1=input()
w2=input()
if len(w1)==len(w2):
        for i in w1:
            for x in w2:
                if i ==x:
                    break
            else:print(False)
        for i in w2:
            for x in w1:        
                if i ==x:
                    break
            else:print(False)
        print(True)      
