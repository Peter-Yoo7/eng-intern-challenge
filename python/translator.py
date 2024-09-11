import sys
braille_dictionary = {
    #Letter in lower Case only  
    'a': 'O.....',  
    'b': 'O.O...',  
    'c': 'OO....',  
    'd': 'OO.O..',  
    'e': 'O..O..',  
    'f': 'OOO...',  
    'g': 'OOOO..',  
    'h': 'O.OO..',  
    'i': '.OO...',  
    'j': '.OOO..',  
    'k': 'O...O.',  
    'l': 'O.O.O.',  
    'm': 'OO..O.',  
    'n': 'OO.OO.',  
    'o': 'O..OO.',  
    'p': 'OOO.O.',  
    'q': 'OOOOO.',  
    'r': 'O.OOO.',  
    's': '.OO.O.',  
    't': '.OOOO.',  
    'u': 'O...OO',  
    'v': 'O.O.OO',  
    'w': '.OOO.O',  
    'x': 'OO..OO',  
    'y': 'OO.OOO', 
    'z': 'O..OOO',  
    
    # Numbers (0-9)
    '1': 'O.....',  
    '2': 'O.O...',  
    '3': 'OO....',  
    '4': 'OO.O..',  
    '5': 'O..O..',  
    '6': 'OOO...',  
    '7': 'OOOO..',  
    '8': 'O.OO..',  
    '9': '.OO...',  
    '0': '.OOO..',  
    
    # Special symbols
    ' ': '......', #space
    'capital': '.....O',   # Capital follows
    'number': '.O.OOO'   # Number follows
}

english_dictionary = {
    'O.....': ['1','a'],   #a as well
    'O.O...': ['2','b'],   #b as well
    'OO....': ['3','c'],   #c as well
    'OO.O..': ['4','d'],   #d as well
    'O..O..': ['5','e'],   #e as well
    'OOO...': ['6','f'],   #f as well
    'OOOO..': ['7','g'],   #g as well
    'O.OO..': ['8','h'],   #h as well
    '.OO...': ['9','i'],   #i as well
    '.OOO..': ['0','j'],   #j as well
    'O...O.': ['k','k'],   
    'O.O.O.': ['l','l'],   
    'OO..O.': ['m','m'],   
    'OO.OO.': ['n','n'],   
    'O..OO.': ['o','o'],   
    'OOO.O.': ['p','p'],   
    'OOOOO.': ['q','q'],   
    'O.OOO.': ['r','r'],   
    '.OO.O.': ['s','s'],  
    '.OOOO.': ['t','t'],   
    'O...OO': ['u','u'],   
    'O.O.OO': ['v','v'],  
    '.OOO.O': ['w','w'],  
    'OO..OO': ['x','x'],  
    'OO.OOO': ['y','y'],  
    'O..OOO': ['z','z'],   
    '.....O': 'capital',  # Capital 
    '.O.OOO': 'number',   # Number 
    '......': [' ', ' ']
}




#helper function to determine if we are braille vs english 
def is_english(input_string):
    for x in input_string:
        if not (x.isalnum() or x.isspace()):
            return False
    return True
  



#sanity check
if len(sys.argv) > 1:
    input_string = sys.argv[1:] #currently have an array of all the values inputed other then the command itself 
    input_string = ' '.join(input_string)
   # print(input_string)
else:
    print("Not enough arguments please try again")
    exit()


if is_english(input_string):
    output = ""
    number = False
    for character in input_string:
        #we need three checks first we need to check if its a number, then if its capital cause they all have different input needed 
        if character.isupper():
            number = False
            output += braille_dictionary['capital']
            output += braille_dictionary[character.lower()]

        elif character.isdigit():
            if not number:
                output += braille_dictionary['number']
                number = True
            output += braille_dictionary[character]
        
        elif not character in braille_dictionary:
            exit()
        else:
            number = False
            output += braille_dictionary[character]

    print(output) 

else:
    output = ""
    capital = False
    number = False
    for i in range(0, len(input_string), 6):
        braille_char = input_string[i:i+6]
        if english_dictionary[braille_char] == "capital":
                capital = True
                continue
        elif english_dictionary[braille_char] == "number":
            number = True
            continue
        # my current error rn is that im not checking if there next character are number or not im just assuming they are not so i need to find a way 
        if braille_char in english_dictionary:
            helper = english_dictionary[braille_char]
            if helper[0].isspace():
                number = False
                output += helper[0]
                continue
            elif number:
                output += helper[0]
                continue
            else:
                helper = helper[1]
                if capital:
                    output += helper.upper()
                    capital = False
                    continue
                output += helper
    print(output)
