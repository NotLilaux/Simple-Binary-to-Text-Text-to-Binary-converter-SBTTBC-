#By NotLilaux on github

#Importing regular expression for string matching
import re

# Settings
DecorationSymbol = '*^'
Option1 = '1'
Option2 = '2'
ExitKey = 'Q' #Preferably uppercase, if otherwise, change the code as you need at line 16.
x=f'''For binary to text conversion, press {Option1}
For text to binary conversion, press {Option2}
Press {ExitKey} for Exit. '''

# Main code
print(DecorationSymbol*25)
answer=input(x)
while answer.upper() != ExitKey:
    print(DecorationSymbol*25)
    if answer == Option1:
        binaryTxt = input('Enter a text in binary code: ')
        if binaryTxt and len(binaryTxt) >= 8:
            binaryTxt = re.findall('[0|1]{8}+', binaryTxt)
            binaryTxtStr = '' 
            for item in binaryTxt:
                binaryTxtStr+=item
            if not binaryTxtStr == '':
                Result=int(binaryTxtStr, 2).to_bytes(len(binaryTxtStr) // 8).decode()
                print(f'''Your text in normal code: 
{Result}''')
            else:
                print('Write a proper text.')

        else:
            print('You haven\'t entered a proper binary or you pressed enter.')
    elif answer == Option2:
        StringTxt = input('Enter a normal text to convert into binary: ')
        Result2 = ' '.join(format(ord(char), '08b') for char in StringTxt)
        print(f'''Your text in binary:
{Result2}''')
    elif answer != Option1 or answer != Option2:
        print(DecorationSymbol*25)
        print(f"User didn't write {Option1} or {Option2}.")
    print(DecorationSymbol*25)
    answer=input(x)

print(DecorationSymbol*25)
print(f"You exited the program using {ExitKey}.")
