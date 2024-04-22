final_accpeting_sates = {}
state_transitionsDeci1 = {"1": "q1" ,"2": "q1" , "3": "q1" , "4": "q1" , "5": "q1" , "6": "q1" ,"7" : "q1" , "8": "q1" ,"9": "q1" , "_": "q3" } 
state_transitionsDeci2 = {"_": "q3", "0": "q5" ,"1": "q5" , "2": "q5" , "3": "q5" ,"4": "q5" ,"5": "q5" ,"6": "q5" ,"7": "q5" ,"8": "q5" ,"9": "q5" ,
                           "a": "q5" , "b": "q5" ,"c": "q5" ,"d": "q5" , "e": "q5" , "f": "q5",
                           "A": "q5" ,"B": "q5" , "C": "q5" , "D": "q5" , "E": "q5" , "F": "q5"}
state_transitionsDeci3 = {"_" : "q8","0" : "q10"}
state_transitionsBin = {"1"}
state_transitionsOcti = {"1"}
state_transitionsHexi = {"1"}

ui = input("Please enter a string")
print("Currently in start state q0. I will now read your input and transition you to the proper states accordingly.")
for index, char in enumerate(ui):
    if index == 0: #if its a deci
        if char != "0":
            print(char + " transitions you into (or keeps you in): " + state_transitionsDeci1[char])
    if index >= 1 and char != "0":
        print(char + " transitions you into (or keeps you in): " + state_transitionsDeci2[char])    
        if char == "_" and index-1 == "_":
            print("Invalid integer literal, contains at least 2 or more underscore in a row.")
            break
    elif index ==1:
        print(" O transitions you into (or keeps you in): q7" )
    elif char == "0":
        print(char + " transitions you into (or keeps you in): " + state_transitionsDeci3[char])




