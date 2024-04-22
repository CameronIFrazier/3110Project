import re

def check_pattern(input_string):
    pattern =  r'^0[xX](_?[0-9a-fA-F])+'

    if re.match(pattern, input_string):
        print("Input follows the pattern.")
    else:
        print("Input does not follow the pattern.")

# Example usage:
input_string = input("Enter a string please")
check_pattern(input_string)
print(input_string)


''' could potentially use a bunch of different try catches
'''