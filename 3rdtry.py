'''
the logic behind this try, is that in order to properly determine whether or not a string is a floating point literal, you must check the string charachter by character 
this loop checks to see: 
 1 if everthing is a digt, a dot, an upper or lowercase e, an underscore, or a dash
 2 underscores must be followed by a digit, there cannot be two repeat underscores 
 3 dashes or plus signs must be follwed by digits

 ******uncertainty***** how do we deal with negatives 
 '''


user_input = input("Please input a literal ")

# Iterate through each index in the string
def check_float(x):
    for char in x:
        if not char in "eE._-":
            if not char.isdigit():
                print("random letters are not allowed in a float")
                return False   
    for i in range(len(x)):
        
        print("Character at index", i, ":", x[i])
        if x[i] == "_":
            if i + 1 < len(x):  # Check if there is a next index
                if not (x[i + 1].isdigit()):
                    print("A digit must follow an underscore.")
                    return False
            else:
                print("An underscore cannot be the last character.")
                return False
        if x[i] in "eE":
            if i + 1 < len(x):  # Check if there is a next index
                if not (x[i + 1].isdigit()):
                   if not(x[i+1] == "-" or x[i+1] == "+"):
                    print("An exponent must be follwed by a digit, a dash, or a plus sign") #isnt a digit, or a dash or plus
                   else:
                       if i + 2 < len(x):   
                           if not (x[i + 2].isdigit()):
                               print("A dash or plus sign must be followed by a digit")
            else:
                print("An exponent cannot be the last character.")
                return False    
        print("The entered value is a floating point literal")
        return True     

print(check_float(user_input))