line = input()
d = {
     '1':'A',
     '2':'B',
     '3':'C',
     '4':'D',
     '5':'E',
     '6':'F',
     '7':'G',
     '8':'H',
     '9':'I',
     '10':'J',
     '11':'K',
     '12':'L',
     '13':'M',
     '14':'N',
     '15':'O',
     '16':'P',
     '17':'Q',
     '18':'R',
     '19':'S',
     '20':'T',
     '21':'U',
     '22':'V',
     '23':'W',
     '24':'X',
     '25':'Y',
     '26':'Z'
     
     }
 
password = list(line)
result_list = []
print(line)
for i in range(len(password)):
    if password[i].isalpha() :       
        for v in d.values():
            if password[i] == v  :
                for k in d:
                    if d[k] == v :
                        password[i] = d[str(26-int(k)+1)]
                break  
            
            if password[i].islower() :                
                if password[i].upper() ==  v :              
                   for k in d:
                        if d[k] == v :
                            password[i] = d[str(26-int(k)+1)].lower()
                   break         
    result_list.append(password[i])
 
for re in result_list:
    print(re,end='')
