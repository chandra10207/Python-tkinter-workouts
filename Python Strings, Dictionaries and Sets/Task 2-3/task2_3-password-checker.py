def checkPassword(pword):

    shortEnough = longEnough = hasUpper = hasLower = hasNumber = hasSpecial = False
    specialChars = '\'~!#$%^*()_+-={}|[]\\:<>?,./'
    
    pwlen = len(pword)
    if(pwlen < 8 or pwlen > 16):        
        return False
    else:
        shortEnough = longEnough = True
        for c in pword:
            if(not hasUpper and c.isupper):
                #print("hhrehe")
                hasUpper = True

            if(not hasLower and c.islower):
                hasLower = True

            if(not hasNumber and c.isdigit):
                hasNumber = True            

            if(not hasSpecial and c in specialChars):
                hasSpecial = True

        if(shortEnough and longEnough and hasUpper and hasLower and hasNumber and hasSpecial):
            return True
        else:
            return False


password = input('Enter your password: ')

if checkPassword(password):
 print('Your password is valid.')
else:
 print('Your password is not valid.')
