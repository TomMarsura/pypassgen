import random
import os

from pyperclip import copy

# / ---------------- VARIABLES ORIGINALES ---------------- \
    
or_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
or_numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
or_symbols = ['!', '@', '#', '$', '%', '&', '*', '-', '_', '+', '=', ';', ':', '/', '?', '~']


# / ---------------- OPTIONS ---------------- \

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['!', '@', '#', '$', '%', '&', '*', '-', '_', '+', '=', ';', ':', '/', '?', '~']
passw = []

majuscules = 1

def genPassword1(nb_chars):
    
    
    nb_nums = random.randint(0, int(nb_chars / 4))
    nb_symb = random.randint(0, int(nb_chars / 4))
    nb_letters = nb_chars - (nb_symb + nb_nums)
    while(nb_chars > 0):
        check = 1
        rand = random.randint(0, 2)
        if rand == 0 and nb_letters > 0:
            randMaj = random.randint(0, 2)
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
    nbChar = nb_letters + nb_nums + nb_symb
    while(nbChar > 0):
        check = 1
        rand = random.randint(0, 2)
        if rand == 0 and nb_letters > 0:
            randMaj = random.randint(0, 2)
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

if __name__ == '__main__':
    print('Welcome to the PyPassword Generator!')    
    user_choice = int(input(" 1. Saisir le nombre de caractères\n 2. Saisir le nombre de chaque caractères\n 3. Options de génération\n Choix : "))
    
    if user_choice == 1:
        nb_letters = 0
        while(nb_letters < 4 or nb_letters > 40):
            nb_letters = int(input("Saisir le nombre de caractères (Entre 4 et 40) : "))
            if nb_letters < 4 or nb_letters > 40 :
                print("Saisie invalide")
        
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
                
                copyPass = ""
                for i in passw:
                    copyPass += i
                
                copy(copyPass)
                print("Mot de passe copié dans le presse-papiers")
    
    elif user_choice == 2:
        nb_letters = int(input("Saisir le nombre de lettres : "))
        nb_nums = int(input("Saisir le nombre de numéros : "))
        nb_symb = int(input("Saisir le nombre de symboles : "))
        
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
                
                copyPass = ""
                for i in passw:
                    copyPass += i
                
                copy(copyPass)
                print("Mot de passe copié dans le presse-papiers")
                
    elif user_choice == 3:
        os.system('cls')
        print("/ --------------- OPTIONS --------------- \\")
        if majuscules:
            print(" 1. Majuscules (Activé)")
        else:
            print(" 1. Majuscules (Désactivé)")
                  
        print(" 2. Retirer des lettres\n 3. Ajouter des lettres")
        print(" 4. Retirer des nombres\n 5. Ajouter des nombres\n 6. Retirer des symboles\n 7. Ajouter des symboles")
            
        