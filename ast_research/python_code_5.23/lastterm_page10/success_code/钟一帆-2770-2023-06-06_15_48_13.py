w1=input()
w2=input()
if len(w1)==len(w2):
    if list(w1).sort()==list(w2).sort():
        print(True)
    
else: print(False)     
