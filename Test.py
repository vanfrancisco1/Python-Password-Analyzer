import re

# Variables
a = ""
PasswordStrength = ""
hasLower = False
hasUpper = False
hasNumber = False
hasSymbol = False

Short = True
print(' ')
print ("PYTHON PASSWORD ANALYZER: ")
a = input("Input password: ")
if (len(a) <= 2):
    print('Password is way too short')
else:
    Short = False
for letter in a:
    if letter.islower():
        hasLower = True
    if letter.isupper():
        hasUpper = True
    if letter.isnumeric():
        hasNumber = True
# Search if word has symbols
regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
if(regex.search(a) == None):
    hasSymbol = False
else:
    hasSymbol = True

# Check if has numbers, uppercase, lowercase and symbol
print("PASSWORD ANALYSIS: ")
print(' ')
print('Lowercase: ' + str(hasLower))
print('Uppercase: ' + str(hasUpper))
print('Numbers: ' + str(hasNumber))
print('Special Characters: ' + str(hasSymbol))
print(' ')
# Numbers Only Conditions
if (len(a) >= 3 and len(a) <= 8):
    if (hasNumber == True):
        PasswordStrength = 'Instantly'
elif(len(a) >= 9 and len(a) <= 18):
    if (a.isdigit() == True):
        if (len(a) == 9):
            PasswordStrength = "4 seconds"
        elif(len(a) == 10):
            PasswordStrength = "40 seconds"
        elif(len(a) == 11):
            PasswordStrength = "6 minutes"
        elif(len(a) == 12):
            PasswordStrength = "1 hour"
        elif(len(a) == 13):
            PasswordStrength = "11 hours"
        elif(len(a) == 14):
            PasswordStrength = "4 days"
        elif(len(a) == 15):
            PasswordStrength = "46 Days"
        elif(len(a) == 16):
            PasswordStrength = "1 year"
        elif(len(a) == 17):
            PasswordStrength = "12 years"
        elif(len(a) == 18):
            PasswordStrength = "126 years"
        else:
            PasswordStrength = 'password way too long'
# UPPERCASE AND LOWERCASE CHECK
if (len(a) >= 3 and len(a) <= 7):
    if (hasLower == True or hasUpper == True):
        PasswordStrength = 'Instantlyy'
elif (len(a) >= 8 and len(a) <= 18):
    if (a.islower() == True or a.isupper() == True):
        if(len(a) == 8):
            PasswordStrength = '13 minutes'
        elif(len(a) == 9):
            PasswordStrength = "6 hours"
        elif(len(a) == 10):
            PasswordStrength = "6 days"
        elif(len(a) == 11):
            PasswordStrength = "169 days"
        elif(len(a) == 12):
            PasswordStrength = "12 years"
        elif(len(a) == 13):
            PasswordStrength = "314 hours"
        elif(len(a) == 14):
            PasswordStrength = "8K years"
        elif(len(a) == 15):
            PasswordStrength = "212K years"
        elif(len(a) == 16):
            PasswordStrength = "512M years"
        elif(len(a) == 17):
            PasswordStrength = "143M years"
        elif(len(a) == 18):
            PasswordStrength = "3B years"
        else:
            PasswordStrength = 'password way too long'
# Mixed Upper and Lower
if (hasLower == True and hasUpper == True):
    if (len(a) >= 3 and len(a) <= 5):
        PasswordStrength = "Instantlyyy"
    elif(len(a) >= 6 and len(a) <= 18):
        if (len(a) == 6):
            PasswordStrength = "8 seconds"
        elif(len(a) == 7):
            PasswordStrength = "5 minutes"
        elif(len(a) == 8):
            PasswordStrength = '3 hours'
        elif(len(a) == 9):
            PasswordStrength = "4 days"
        elif(len(a) == 10):
            PasswordStrength = "169 days"
        elif(len(a) == 11):
            PasswordStrength = "16 years"
        elif(len(a) == 12):
            PasswordStrength = "600 years"
        elif(len(a) == 13):
            PasswordStrength = "21k years"
        elif(len(a) == 14):
            PasswordStrength = "778k years"
        elif(len(a) == 15):
            PasswordStrength = "28M years"
        elif(len(a) == 16):
            PasswordStrength = "1B years"
        elif(len(a) == 17):
            PasswordStrength = "36B years"
        elif(len(a) == 18):
            PasswordStrength = "1TN years"
        else:
            PasswordStrength = 'password way too long'
# Mixed Lower, Upper and Numbers
if (hasLower == True and hasUpper == True and hasNumber == True):
        if (len(a) >= 3 and len(a) <= 4):
            PasswordStrength = "Instantlyyyy"
        elif (len(a)>= 5 and len(a) <= 18):
            if(len(a) == 5):
                PasswordStrength = "3 seconds"
            elif (len(a) == 6):
                PasswordStrength = "3 minutes"
            elif(len(a) == 7):
                PasswordStrength = "3 hours"
            elif(len(a) == 8):
                PasswordStrength = '10 days'
            elif(len(a) == 9):
                PasswordStrength = "1 year"
            elif(len(a) == 10):
                PasswordStrength = "106 years"
            elif(len(a) == 11):
                PasswordStrength = "6K years"
            elif(len(a) == 12):
                PasswordStrength = "108K years"
            elif(len(a) == 13):
                PasswordStrength = "25M years"
            elif(len(a) == 14):
                PasswordStrength = "1B years"
            elif(len(a) == 15):
                PasswordStrength = "97B years"
            elif(len(a) == 16):
                PasswordStrength = "6TN years"
            elif(len(a) == 17):
                PasswordStrength = "374TN years"
            elif(len(a) == 18):
                PasswordStrength = "23QD years"
            else:
                PasswordStrength = 'password way too long'
if (hasLower == True and hasUpper == True and hasNumber == True and hasSymbol == True):
        if (len(a) >= 3 and len(a) <= 4):
            PasswordStrength = "Instantlyyyy"
        elif (len(a)>= 5 and len(a) <= 18):
            if(len(a) == 5):
                PasswordStrength = "10 seconds"
            elif (len(a) == 6):
                PasswordStrength = "13 minutes"
            elif(len(a) == 7):
                PasswordStrength = "17 hours"
            elif(len(a) == 8):
                PasswordStrength = '57 days'
            elif(len(a) == 9):
                PasswordStrength = "12 years"
            elif(len(a) == 10):
                PasswordStrength = "928 years"
            elif(len(a) == 11):
                PasswordStrength = "71K years"
            elif(len(a) == 12):
                PasswordStrength = "5M years"
            elif(len(a) == 13):
                PasswordStrength = "423M years"
            elif(len(a) == 14):
                PasswordStrength = "5B years"
            elif(len(a) == 15):
                PasswordStrength = "2TN years"
            elif(len(a) == 16):
                PasswordStrength = "193TN years"
            elif(len(a) == 17):
                PasswordStrength = "14QD years"
            elif(len(a) == 18):
                PasswordStrength = "1QT years"
            else:
                PasswordStrength = 'password way too long'          

#Password Output
if (Short == False):
    print("PASSWORD RESULT: ")
    print("Length of Password: " + str(len(a)))
    print('PASSWORD STRENGTH: ' + PasswordStrength)
            

