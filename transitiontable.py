state_transitiontable_table = {
    'q0': {'-': 'q7'},

    'q8': {'B':'q13', 'b': 'q13', "_": 'rejected'},
    'q11': {'0':'binary accepting state', '1':'binary accepting state'},  
    'q13': {"_":'q11', '0':'binary accepting state', '1':'binary accepting state'},
    'binary accepting state': {'0': 'binary accepting state', '1': 'binary accepting state', "_": 'q11'},

    
    'q26': {'X':'q28', 'x': 'q28', "_": 'rejected'},
    'q29': {'0':'hexi accepting state', '1':'hexi accepting state', '2':'hexi accepting state', '3':'hexi accepting state', '4':'hexi accepting state',
            '5':'hexi accepting state', '6':'hexi accepting state', '7':'hexi accepting state', '8':'hexi accepting state', '8':'hexi accepting state'
            , 'A':'hexi accepting state', 'B':'hexi accepting state', 'C':'hexi accepting state', 'D':'hexi accepting state', 'E':'hexi accepting state'
            , 'F':'hexi accepting state'
            , 'a':'hexi accepting state', 'b':'hexi accepting state', 'c':'hexi accepting state', 'd':'hexi accepting state', 'e':'hexi accepting state'
            , 'f':'hexi accepting state'},  
    'q28': {'0':'hexi accepting state', '1':'hexi accepting state', '2':'hexi accepting state', '3':'hexi accepting state', '4':'hexi accepting state',
            '5':'hexi accepting state', '6':'hexi accepting state', '7':'hexi accepting state', '8':'hexi accepting state', '8':'hexi accepting state'
            , 'A':'hexi accepting state', 'B':'hexi accepting state', 'C':'hexi accepting state', 'D':'hexi accepting state', 'E':'hexi accepting state'
            , 'F':'hexi accepting state'
            , 'a':'hexi accepting state', 'b':'hexi accepting state', 'c':'hexi accepting state', 'd':'hexi accepting state', 'e':'hexi accepting state'
            , 'f':'hexi accepting state', '_': 'q29'},
    'hexi accepting state': {'0':'hexi accepting state', '1':'hexi accepting state', '2':'hexi accepting state', '3':'hexi accepting state', '4':'hexi accepting state',
            '5':'hexi accepting state', '6':'hexi accepting state', '7':'hexi accepting state', '8':'hexi accepting state', '8':'hexi accepting state'
            , 'A':'hexi accepting state', 'B':'hexi accepting state', 'C':'hexi accepting state', 'D':'hexi accepting state', 'E':'hexi accepting state'
            , 'F':'hexi accepting state'
            , 'a':'hexi accepting state', 'b':'hexi accepting state', 'c':'hexi accepting state', 'd':'hexi accepting state', 'e':'hexi accepting state'
            , 'f':'hexi accepting state', "_": 'q29'},

    
    'q15': {'O':'q24', 'o': 'q24', "_": 'rejected'},
    'q23': {'0':'octa accepting state', '1':'octa accepting state', '2':'octa accepting state', '3':'octa accepting state', '4':'octa accepting state',
            '5':'octa accepting state', '6':'octa accepting state', '7':'octa accepting state'},  
    'q24': {'0':'octa accepting state', '1':'octa accepting state', '2':'octa accepting state', '3':'octa accepting state', '4':'octa accepting state',
            '5':'octa accepting state', '6':'octa accepting state', '7':'octa accepting state', '_':'q23'},
    'octa accepting state': {'0':'octa accepting state', '1':'octa accepting state', '2':'octa accepting state', '3':'octa accepting state', '4':'octa accepting state',
            '5':'octa accepting state', '6':'octa accepting state', '7':'octa accepting state', '_':'q23'}

}

temp = 'q0'
ui = input("Please enter a string")

for index, char in enumerate(ui):
    if char == '0' and index + 1 < len(ui) and (ui[index + 1] == 'b' or ui[index + 1] == 'B'):
        temp = 'q8'
        print("You are now in " + temp)
        continue
    if char == '0' and index + 1 < len(ui) and (ui[index + 1] == 'x' or ui[index + 1] == 'X'):
        temp = 'q26'
        print("You are now in " + temp)
        continue
    if char == '0' and index + 1 < len(ui) and (ui[index + 1] == 'o' or ui[index + 1] == 'O'):
        temp = 'q15'
        print("You are now in " + temp)
        continue

    temp = state_transitiontable_table[temp][char]
    print("you are now in " + str(temp))

if temp =='hexi accpeting state' or temp == 'octa accepting state' or temp == 'binary accepting state':
    print("Valid Literal")
        
       
'''need to put try catch around trans table in case the string contains something not in the dictionary'''