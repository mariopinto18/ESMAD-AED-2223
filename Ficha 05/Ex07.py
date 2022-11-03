
import random

# função geradora de passwords
def generatePassword(userName):
    """
    Generate a password based on the username
    """
    if userName.find(" ")!= -1:
        return "username Inválido!"
    
    password = ""        # password é constituída por essa posição, seguido de random
    for i in range(1, len(userName), 2):       
        password+= userName[i] + str(random.randint(1,9))     
    password+= str(len(userName))
    return password


userName = input("Username:")
passwd= generatePassword(userName)
print("password:{0}" .format(passwd))

