state_transitions = {
    'q0': {'1':'deci accepting state', '2':'deci accepting state', '3':'deci accepting state', '4':'deci accepting state', '5':'deci accepting state',
           '6':'deci accepting state', '7':'deci accepting state', '8':'deci accepting state', '9':'deci accepting state'},
    'q19':{'0':'deci accepting state','1':'deci accepting state', '2':'deci accepting state', '3':'deci accepting state', '4':'deci accepting state', '5':'deci accepting state',
        '6':'deci accepting state', '7':'deci accepting state', '8':'deci accepting state', '9':'deci accepting state'},
    'deci accepting state': {'0':'deci accepting state','1':'deci accepting state', '2':'deci accepting state', '3':'deci accepting state', '4':'deci accepting state', '5':'deci accepting state',
        '6':'deci accepting state', '7':'deci accepting state', '8':'deci accepting state', '9':'deci accepting state', "_": 'q19'},


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
            '5':'octa accepting state', '6':'octa accepting state', '7':'octa accepting state', '_':'q23'},

}


temp = 'q0'
ui = input("Please enter a string with no spaces: ")

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
    try:
        temp = state_transitions[temp][char]
        print("You are now in " + str(temp))
    except KeyError:
        print("Invalid Literal. You entered a character that isn't acceptable. Keep in mind there can be no spaces or special character in a literal.")
        temp = "rejected"
        break

if temp =='hexi accepting state' or temp == 'octa accepting state' or temp == 'binary accepting state' or temp == 'deci accepting state':
    print("Valid Literal")
else:
    print("Invalid Literal")
        



       
