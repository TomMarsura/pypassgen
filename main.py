import random
import os
from pyperclip import copy

# / ---------------- MENUS ---------------- \

WELCOME_PRINT = """###############################################
########## PYTHON PASSWORD GENERATOR ##########
###############################################
"""

OPTIONS_PRINT = """###############################################
################### OPTIONS ###################
###############################################
"""

DELLET_PRINT = """##############################################
############ SUPRESSION DE LETTRE ############
##############################################

"""

ADDLET_PRINT = """###############################################
############### AJOUT DE LETTRE ###############
###############################################

"""

DELNUM_PRINT = """##############################################
############ SUPRESSION DE NOMBRE #############
##############################################

"""

ADDNUM_PRINT = """###############################################
############### AJOUT DE NOMBRE ###############
###############################################

"""

DELSYM_PRINT = """##############################################
############ SUPRESSION DE SYMBOLE ############
###############################################

"""

ADDSYM_PRINT ="""###############################################
############### AJOUT DE SYMBOLE ###############
################################################

"""
RESTORE_PRINT = """###############################################
################# RESTAURATION #################
################################################

"""

# / ---------------- ORIGINAL VARIABLES ---------------- \
    
or_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
or_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
or_symbols = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']


# / ---------------- OPTIONS ---------------- \

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
passw = []

majuscules = 1

# / ---------------- CHOICES LIST ---------------- \
    
symbols_1 = ['!', '#', '$', '%', '&', '*', '+', '-', '.', '/', ':', ';', '=', '?', '@', '^', '_', '`', '~']
symbols_2 = ['"', '(', ')', ',', '<', '>', '[', '\\', ']', '{', '|', '}']
symbols_3 = ['%', '(', ')', '*', '+', ',', '-', '/', ':', ';', '<', '=', '>', '_', '{', '}']
symbols_4 = ['!', '#', '$', '*', '-', '/', ';', '?', '@', '^', '_', '`', '~']

# / ---------------- FUNCTIONS ---------------- \

def genPassword1(nb_chars):
    
    """ Function that generates a password from a number of characters from the parameter """

    """ Randomize the number of symbols, numbers and letters for the password """
    nb_nums = random.randint(0, int(nb_chars / 4))
    nb_symb = random.randint(0, int(nb_chars / 4))
    nb_letters = nb_chars - (nb_symb + nb_nums)

    """ Generating the password """
    while(nb_chars > 0):
        check = 1
        rand = random.randint(0, 2)
        if rand == 0 and nb_letters > 0:
            if majuscules == 1:
                randMaj = random.randint(0, 2)
            else:
                randMaj = 0
            if randMaj <= 1:
                passw.append(letters[random.randint(0, int(len(letters) - 1))])
            else:
                passw.append(letters[random.randint(0, int(len(letters) - 1))].upper())
            nb_letters -= 1
            check = 0
        elif rand == 1 and nb_nums:
            passw.append(numbers[random.randint(0, int(len(numbers) - 1))])
            nb_nums -= 1
            check = 0
        elif rand == 2 and nb_symb:
            passw.append(symbols[random.randint(0, int(len(symbols) - 1))])
            nb_symb -= 1
            check = 0
        if check == 0:
            nb_chars -= 1

def genPassword2(nb_letters, nb_nums, nb_symb):
    """ Function that generates a password from a given number of letters, symbols and numbers """

    nbChar = nb_letters + nb_nums + nb_symb

    """ Generating the password """
    while(nbChar > 0):
        check = 1
        rand = random.randint(0, 2)
        if rand == 0 and nb_letters > 0:
            if majuscules == 1:
                randMaj = random.randint(0, 2)
            else:
                randMaj = 0
            if randMaj <= 1:
                passw.append(letters[random.randint(0, int(len(letters) - 1))])
            else:
                passw.append(letters[random.randint(0, int(len(letters) - 1))].upper())
            nb_letters -= 1
            check = 0
        elif rand == 1 and nb_nums:
            passw.append(numbers[random.randint(0, int(len(numbers) - 1))])
            nb_nums -= 1
            check = 0
        elif rand == 2 and nb_symb:
            passw.append(symbols[random.randint(0, int(len(symbols) - 1))])
            nb_symb -= 1
            check = 0
        if check == 0:
            nbChar -= 1

def genPassword3(nb_chars, symb):
    
    """ Function that generates a password from a given number of chars and a list of symbols alredy defined """
    nb_nums = random.randint(0, int(nb_chars / 3))
    nb_symb = random.randint(0, int(nb_chars / 3))
    nb_letters = nb_chars - (nb_symb + nb_nums)

    """ Generating the password """
    while(nb_chars > 0):
        check = 1
        rand = random.randint(0, 2)
        if rand == 0 and nb_letters > 0:
            if majuscules == 1:
                randMaj = random.randint(0, 2)
            else:
                randMaj = 0
            if randMaj <= 1:
                passw.append(letters[random.randint(0, int(len(letters) - 1))])
            else:
                passw.append(letters[random.randint(0, int(len(letters) - 1))].upper())
            nb_letters -= 1
            check = 0
        elif rand == 1 and nb_nums:
            passw.append(numbers[random.randint(0, int(len(numbers) - 1))])
            nb_nums -= 1
            check = 0
        elif rand == 2 and nb_symb:
            if symb == 1:
                passw.append(symbols_1[random.randint(0, int(len(symbols_1) - 1))])
            if symb == 2:
                passw.append(symbols_2[random.randint(0, int(len(symbols_2) - 1))])
            if symb == 3:
                passw.append(symbols_3[random.randint(0, int(len(symbols_3) - 1))])
            if symb == 4:
                passw.append(symbols_4[random.randint(0, int(len(symbols_4) - 1))])
            nb_symb -= 1
            check = 0
        if check == 0:
            nb_chars -= 1

def delChar(charType, char):

    """ Function which ables the user to delete characters from the list given by the app to generate a password """


    """ Treating the exceptions from the given parameters """
    if charType == 0 and len(letters) > 0:
        if char.lower() in letters:
            letters.remove(char.lower())
        else:
            print("Erreur : caractère non trouvé dans la liste des lettres")

    elif charType == 0 and len(letters) == 0:
        print("Erreur : la liste des lettres est vide")

    elif charType == 1 and len(numbers) > 0:
        if char in numbers:
            numbers.remove(char)
        else:
            print("Erreur : caractère non trouvé dans la liste des nombres")
            
    elif charType == 1 and len(numbers) == 0:
        print("Erreur : la liste des nombres est vide")
            
    elif charType == 2 and len(symbols) > 0:
        if char in symbols:
            symbols.remove(char)
        else:
            print("Erreur : caractère non trouvé dans la liste des symboles")
        
    elif charType == 2 and len(symbols) == 0:
        print("Erreur : la liste des symboles est vide")

def addChar(charType, char): 
    """ 
        charType : 0 = letter, 1 = number, 2 = symbol
        If all the letters are already enabled, the user can't add another letter
        If all the numbers are already enabled, the user can't add another number
        If all the symbols are already enabled, the user can't add another symbol
        Original list in the part 'ORIGINAL VARIABLES'
    """

    """ Treating exceptions from the give parameters """
    
    if charType == 0:
        if len(letters) == len(or_letters):
            print("Erreur : toutes les lettres sont déjà présentes")
        elif char.lower() in letters:
            print("Erreur : le caractère est déjà présent dans la liste")
        elif char.lower() not in or_letters:
            print("Erreur : ce caractère n'est pas une lettre")
        else:
            letters.append(char.lower())
    elif charType == 1:
        if len(numbers) == len(or_numbers):
            print("Erreur : tous les nombres sont déjà présents")
        elif char in numbers:
            print("Erreur : le caractère est déjà présent dans la liste")
        elif char not in or_numbers:
            print("Erreur : ce caractère n'est pas un nombre")
        else:
            numbers.append(char)
    elif charType == 2:
        if len(symbols) == len(or_symbols):
            print("Erreur : tous les symboles sont déjà présents")
        elif char in symbols:
            print("Erreur : le caractère est déjà présent dans la liste")
        elif char in or_letters or char in or_numbers:
            print("Erreur : ce caractère n'est pas un symbole")
        else:
            symbols.append(char)

def displayChar(charType):

    """ Function that displays the characters used to generate the password. The charType represents the type of character to be displayed """

    if charType == 0:
        for i in range(len(letters)):
            print(f"{letters[i].upper()}|", end="")
        
        print("\n")
    
    elif charType == 1:
        for i in range(len(numbers)):
            print(f"{numbers[i]}|", end="")
        
        print("\n")
    
    elif charType == 2:
        for i in range(len(symbols)):
            print(f"{symbols[i]}|", end="")
        
        print("\n")

if __name__ == '__main__':
    """ Main function which makes the generator displayed on the screen """
    #VARIABLE USED TO QUIT THE APP WHEN THE VALUE IS 0
    keepgen = 1
    
    #ORIGINAL VARIABLES
    nb_letters = -1
    nb_nums = -1
    nb_symb = -1
    
    user_choice = 0
    user_choice2 = -1

    """ Loop which makes the generator displayed on the sceen """
    while(keepgen == 1):
        nb_letters = -1
        nb_nums = -1
        nb_symb = -1
        
        """ Displaying the main menu """
        os.system('cls')
        print(WELCOME_PRINT)    
        user_choice = int(input("| 1. Saisir le nombre de caractères\n| 2. Saisir le nombre de chaque caractères\n| 3. Choix complet\n| 4. Options de génération\n| 5. Quitter\n\n| Choix : "))
        
        """ Treating the choice of the user """

        if user_choice == 1:

            """ Choice 1 : Generates a password with a number of characters given """

            nb_letters = 0
            while(nb_letters < 4 or nb_letters > 40):
                nb_letters = int(input("Saisir le nombre de caractères (Entre 4 et 40) : "))
                if nb_letters < 4 or nb_letters > 40 :
                    print("Saisie invalide")
            
            """ Variable which enables the user to restart the generation while the password is not good enough for him """
            restart = 1
            while(restart == 1):
                genPassword1(nb_letters)
                print("Votre mot de passe généré est : ", end='')
                for i in range(len(passw)):
                    print(passw[i], end='')
                user_choice = int(input("\nVoulez vous recréer un nouveau mot de passe ? (1: Oui | 0: Non) "))
                
                if user_choice == 1:
                    restart = 1
                    passw = []
                else:
                    restart = 0
                    
                    user_choice2 = -1
                    while(user_choice2 != 1 and user_choice2 != 0):
                        user_choice2 = int(input("Voulez vous copier le mot de passe dans le presse-papiers ? (1: Oui | 0: Non) "))
                    
                    if user_choice2 == 1:
                        copyPass = ""
                        for i in passw:
                            copyPass += i
                        
                        copy(copyPass)
                        print("Mot de passe copié dans le presse-papiers")
        
        elif user_choice == 2:

            """ Choice 2 : Generates a password with a number of each characters given """

            while nb_letters < 0:
                nb_letters = int(input("Saisir le nombre de lettres : "))
            while nb_nums < 0:
                nb_nums = int(input("Saisir le nombre de numéros : "))
            while nb_symb < 0:
                nb_symb = int(input("Saisir le nombre de symboles : "))
            
            """ Variable which enables the user to restart the generation while the password is not good enough for him """
            
            restart = 1
            while(restart == 1):
                genPassword2(nb_letters, nb_nums, nb_symb)
                print("Votre mot de passe généré est : ", end='')
                for i in range(len(passw)):
                    print(passw[i], end='')
                user_choice = int(input("\nVoulez vous recréer un nouveau mot de passe ? (1: Oui | 0: Non) "))
                
                if user_choice == 1:
                    restart = 1
                    passw = []
                else:
                    restart = 0
                    
                    user_choice2 = -1
                    while(user_choice2 != 1 and user_choice2 != 0):
                        user_choice2 = int(input("Voulez vous copier le mot de passe dans le presse-papiers ? (1: Oui | 0: Non) "))
                    
                    if user_choice2 == 1:
                        copyPass = ""
                        for i in passw:
                            copyPass += i
                        
                        copy(copyPass)
                        print("Mot de passe copié dans le presse-papiers")

        elif user_choice == 3:
            
            """ Choice 3 : Generates a password with a preset of symbols and a number of characters given  """

            os.system('cls')
            print(" 1. ", end='')
            for i in range(len(symbols_1)):
                print(f"{symbols_1[i]}", end='')
            print('\n')
            print(" 2. ", end='')
            for i in range(len(symbols_2)):
                print(f"{symbols_2[i]}", end='')
            print('\n')
            print(" 3. ", end='')
            for i in range(len(symbols_3)):
                print(f"{symbols_3[i]}", end='')
            print('\n')
            print(" 4. ", end='')
            for i in range(len(symbols_4)):
                print(f"{symbols_4[i]}", end='')
            print('\n')
            
            user_choice2 = 0
            while(user_choice2 < 1 or user_choice2 > 4):
                user_choice2 = int(input("Sélectionner le presets de symboles à utiliser (1 à 4) : "))
                if user_choice2 < 1 or user_choice2 > 4:
                    print("Choix incorrect !")
                    
            nb_letters = int(input("Saisir le nombre de caractères à utiliser : "))

            """ Variable which enables the user to restart the generation while the password is not good enough for him """

            restart = 1
            while(restart == 1):
                genPassword3(nb_letters, user_choice2)
                print("Votre mot de passe généré est : ", end='')
                for i in range(len(passw)):
                    print(passw[i], end='')
                user_choice = int(input("\nVoulez vous recréer un nouveau mot de passe ? (1: Oui | 0: Non) "))
                
                if user_choice == 1:
                    restart = 1
                    passw = []
                else:
                    restart = 0
                    
                    user_choice2 = -1
                    while(user_choice2 != 1 and user_choice2 != 0):
                        user_choice2 = int(input("Voulez vous copier le mot de passe dans le presse-papiers ? (1: Oui | 0: Non) "))
                    
                    if user_choice2 == 1:
                        copyPass = ""
                        for i in passw:
                            copyPass += i
                        
                        copy(copyPass)
                        print("Mot de passe copié dans le presse-papiers")
                    
        elif user_choice == 4:

            """ CHOICE 4 : Change the parameters of the generator """

            user_choice2 = 0
            while user_choice2 != 9:
                user_choice2 = 0
                while(1 > user_choice2 or user_choice2 > 9):
                    os.system('cls')
                    print(OPTIONS_PRINT)
                    if majuscules:
                        print("| 1. Majuscules (Activé)")
                    else:
                        print("| 1. Majuscules (Désactivé)")
                            
                    print("| 2. Retirer des lettres\n| 3. Ajouter des lettres")
                    print("| 4. Retirer des nombres\n| 5. Ajouter des nombres\n| 6. Retirer des symboles\n| 7. Ajouter des symboles")
                    user_choice2 = int(input("| 8. Restaurer les paramètres par défaut\n| 9. Retour\n\n| Choix : "))
                
                if user_choice2 == 1:
                    if majuscules:
                        majuscules = 0
                    else:
                        majuscules = 1
                elif user_choice2 == 2:
                    user_choice3 = ''
                    while(user_choice3 != '-1' and len(letters) > 0):
                        os.system('cls')
                        print(DELLET_PRINT)
                        displayChar(0)
                        user_choice3 = input("Saisir la lettre à retirer (\"-1\" pour quitter) : ")
                        if user_choice3 != '-1':
                            delChar(0, user_choice3)
                    if (len(numbers)) == 0:
                        print("Il n'y a plus de lettres dans la liste !")
                elif user_choice2 == 3:
                    user_choice3 = ''
                    while(user_choice3 != '-1' and len(letters) < len(or_letters)):
                        os.system('cls')
                        print(ADDLET_PRINT)
                        letters.sort()
                        displayChar(0)
                        user_choice3 = input("Saisir la lettre à ajouter (\"-1\" pour quitter) : ")
                        if user_choice3 != '-1':
                            addChar(0, user_choice3)     
                    if len(letters) == len(or_letters):
                        os.system('cls')
                        print(ADDLET_PRINT)
                        letters.sort()
                        displayChar(0)
                        input("Le nombre maximum de lettres a été atteint !")           
                elif user_choice2 == 4:
                    user_choice3 = ''
                    while(user_choice3 != '-1' and len(numbers) > 0):
                        os.system('cls')
                        print(DELNUM_PRINT)
                        displayChar(1)
                        user_choice3 = input("Saisir le nombre à retirer (\"-1\" pour quitter) : ")
                        if user_choice3 != '-1':
                            delChar(1, user_choice3)  
                    if len(numbers) == 0:
                        input("La liste des nombres est vide !") 
                elif user_choice2 == 5:
                    user_choice3 = ''
                    while(user_choice3 != '-1' and len(numbers) < len(or_numbers)):
                        os.system('cls')
                        print(ADDNUM_PRINT)
                        numbers.sort()
                        displayChar(1)
                        user_choice3 = input("Saisir le nombre à ajouter (\"-1\" pour quitter) : ")
                        if user_choice3 != '-1':
                            addChar(1, user_choice3)
                    if len(numbers) == len(or_numbers):
                        os.system('cls')
                        print(ADDNUM_PRINT)
                        numbers.sort()
                        displayChar(1)
                        input("Le nombre maximum de nombres a été atteint !")
                elif user_choice2 == 6:
                    user_choice3 = ''
                    while(user_choice3 != '-1' and len(symbols) > 0):
                        os.system('cls')
                        print(DELSYM_PRINT)
                        displayChar(2)
                        user_choice3 = input("Saisir le symbole à retirer (\"-1\" pour quitter) : ")
                        if user_choice3 != '-1':
                            delChar(2, user_choice3)  
                    if len(symbols) == 0:
                        input("La liste des symboles est vide !")
                elif user_choice2 == 7:
                    user_choice3 = ''
                    while(user_choice3 != '-1' and len(symbols) < len(or_symbols) and len(user_choice3) <= 1):
                        os.system('cls')
                        print(ADDSYM_PRINT)
                        symbols.sort()
                        displayChar(2)
                        user_choice3 = input("Saisir le symbole à ajouter (\"-1\" pour quitter) : ")
                        if user_choice3 != '-1':
                            addChar(2, user_choice3)  
                    if len(symbols) == len(or_symbols):
                        os.system('cls')
                        print(ADDSYM_PRINT)
                        symbols.sort()
                        displayChar(2)
                        input("Le nombre maximum de symboles a été atteint !")
                elif user_choice2 == 8:
                    os.system('cls')
                    print(RESTORE_PRINT)
                    displayChar(0)
                    displayChar(1)
                    displayChar(2)
                    user_choice3 = ''
                    while(user_choice3 != 2 and user_choice3 != 1):
                        user_choice3 = int(input("Voulez-vous vraiment restaurer les paramètres par défaut ? (1. Oui | 2. Non) : "))
                        if user_choice3 != 2 and user_choice3 != 1:
                            print("Choix incorrect !")
                    
                    if user_choice3 == 1:
                        majuscules = 1
                        letters = or_letters.copy()
                        numbers = or_numbers.copy()
                        symbols = or_symbols.copy()
                elif user_choice2 == 9:
                    pass
            if user_choice == 9:
                pass
         
        elif user_choice == 5:

            """ Choice 5 : Leave the generator """

            keepgen = 0
            os.system('cls')
            print("\n\n Merci d'avoir utilisé ce générateur de mot de passe ! A bientôt !\n\n")
            
        passw = []