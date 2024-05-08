import time, sys, random, os
from os import system

# A la ligne 11 et 436, il faut cree des fichiers et de mettre leur lieu sur le programme 
# J'ai fait des fichiers pour mieux organiser mon ordinateur

system('cls') # Vide le "Terminal"

def animation(filenames, frame_time, times):
    # ICI
    os.chdir("C:\\Users\\aydip\\Projet informatique\\animations") # Lieu d'un fichier pour des animations
    frames = []
    for name in filenames:
        with open(name, 'r', encoding='utf8') as f:
            frames.append(f.readlines())
        
    for i in range(times):
        for frame in frames:
            print("".join(frame))
            time.sleep(frame_time)
            os.system('cls')


def attaque(class_du_joueur):
    if class_du_joueur == "Sorcier":
        #attaque_type = random.choice["Potion de poison",""]
        attaque_type = "Potion de poison"

    elif class_du_joueur == "Samouraï":
        #attaque_type = random.choice["Coup d'épée", ""]
        attaque_type = "Coup d'épée"

    elif class_du_joueur == "Archer":
        #attaque_type = random.choice["Tire l'arc à flèches", ""]
        attaque_type = "Tirer l'arc à flèches"

    elif class_du_joueur == "Guérisseur":
        #attaque_type = random.choice["Guérir",""]
        attaque_type = "Guérir"

    attaque = affichage_énnoncé(attaque_type, 'Soigner', 'Blocker', 'Courrir')
    
    return attaque


def affichage_énnoncé(un,deux,trois,quatre):
    while True:
        if trois == None and quatre == None:
            print(f"""
            1. {un}
            2. {deux}
            """)

        elif quatre == None:
            print(f"""
            1. {un}
            2. {deux}
            3. {trois}
            """)

        else:
            print(f"""
            1. {un}
            2. {deux}
            3. {trois}
            4. {quatre}
            """)

        time.sleep(0.5)

        choix = input(">>> ")

        if trois == None and quatre == None and choix == '1' or choix == '2':
            return choix
        
        elif quatre == None and choix == '1' or choix == '2' or choix == '3':
            return choix
        
        elif choix == '1' or choix == '2' or choix == '3' or choix == '4':
            return choix

        else:
            print('\nOrdinateur: Je ne comprends pas.\n')    
    

def introduction():
    print("Ordinateur: Bonjour et bienvenue à Clash des héros.")
    time.sleep(1.5)
    print("Ordinateur: Veut-tu jouer?")
    time.sleep(1.5)

    debuter = affichage_énnoncé('Oui','Non', None, None)
    time.sleep(2)
    system('cls')

    if debuter == '1':
        print("Ordinateur: Parfait! Entre le nom de ton Héro.")
        time.sleep(1)
        nom_du_joueur = input(">>> ").strip()
        time.sleep(3)
        system('cls')

        deja_un_compte = entrer(nom_du_joueur)
        
        if not deja_un_compte:
            if len(nom_du_joueur) > 2:
                time.sleep(1)
                print(f"Ordinateur: Bonjour {nom_du_joueur}!")
                print("Ordinateur: Maintenant, il faut choisir une class.")
                class_du_joueur = affichage_énnoncé("Sorcier", "Samouraï", "Archer", "Guérisseur")
                
                if class_du_joueur == '1':
                    class_du_joueur = "Sorcier"
                
                elif class_du_joueur == '2':
                    class_du_joueur = "Samouraï"

                elif class_du_joueur == '3':
                    class_du_joueur = 'Archer'

                elif class_du_joueur == '4':
                    class_du_joueur = 'Guérisseur'

                print(f"\nOrdinateur: {nom_du_joueur} le {class_du_joueur}.")
                
                return [nom_du_joueur,deja_un_compte,class_du_joueur]
        
        else:
            return [nom_du_joueur,deja_un_compte]


    elif debuter == '2':
        fichiers = ['x1.txt','x2.txt','x3.txt']
        animation(fichiers, 0.3, 5)
        print("\nÀ la prochaine ;(")
        time.sleep(2)
        system('cls')
        sys.exit()  



def combat(nombre_enemy, class_du_joueur):
    
    print(f"\nOrdinateur: Fait attention!\nOrdinateur: Il y a {nombre_enemy} enemys!")

    combat = True

    # Class de l'hero

    if class_du_joueur == "Samouraï":
        statistique_joueur = {
            "HP": 100,
            "Mana": 100,
            "Puissance": 35,
            "Niveau": 1,
            "EXP": 0,
            "Soins": 10,
            "HP Base": 100,
            "Defi": 0 
        }

    elif class_du_joueur == "Sorcier":
        statistique_joueur = {
            "HP": 80,
            "Mana": 150,
            "Puissance": 20,
            "Niveau": 1,
            "EXP": 0,
            "Soins": 15,
            "HP Base": 100,
            "Defi": 0 
        }

    elif class_du_joueur == "Archer":
        statistique_joueur = {
            "HP": 125,
            "Mana": 80,
            "Puissance": 25,
            "Niveau": 1,
            "EXP": 0,
            "Soins": 5,
            "HP Base": 100,
            "Defi": 0
        }

    elif class_du_joueur == "Guérisseur":
        statistique_joueur = {
            "HP": 100,
            "Mana": 100,
            "Puissance": 13,
            "Niveau": 1,
            "EXP": 0,
            "Soins": 25,
            "HP Base": 100,
            "Defi": 0 
        }

    # Class des enemys selon le niveau

    if statistique_joueur["Niveau"] < 4:
        # Faible
        statistique_enemy = {
            "HP": 100,
            "Mana": 100,
            "Puissance": 12,
            "Niveau": 5,
            "EXP": 100,
            "Soins": 10,
            "Puissance Base": 12
        }
    
    elif statistique_joueur["Niveau"] == 5:
        # Moyen
        statistique_enemy = {
            "HP": 150,
            "Mana": 100,
            "Puissance": 12,
            "Niveau": 5,
            "EXP": 100,
            "Soins": 10,
            "Puissance Base": 12
        }
    
    elif statistique_joueur["Niveau"] > 5:
        # Fort
        statistique_enemy = {
            "HP": 200,
            "Mana": 100,
            "Puissance": 12,
            "Niveau": 5,
            "EXP": 100,
            "Soins": 10,
            "Puissance Base": 12
        }

    while combat:
        statistique_enemy["Puissance"] = statistique_enemy["Puissance Base"]
        choix_attaque = attaque(class_du_joueur)

        # Attaque 
        if choix_attaque == '1':

            if statistique_enemy["HP"] - statistique_joueur["Puissance"] > 1:
                statistique_enemy["HP"] -= statistique_joueur["Puissance"]
                print(f'\nEnemy: \033[31m-{statistique_joueur["Puissance"]} HP\033[0m')
                print(f'Enemy: J\'ai {statistique_enemy["HP"]} HP') 
            


            else:
                nombre_enemy -= 1
                statistique_enemy["HP"] = 100
                print(f"\nOrdinateur: Tu as tués 1 gobelin\nOrdinateur: Il te reste {nombre_enemy} enemys.\n\033[32m+{statistique_enemy['EXP']} EXP\033[0m")
                statistique_joueur["EXP"] += statistique_enemy["EXP"]


        
        # Soigner
        if choix_attaque == '2':
            if statistique_joueur['HP'] + statistique_joueur['Soins'] > statistique_joueur["HP Base"] :
                statistique_joueur['HP'] = statistique_joueur['HP Base']
            else:
                statistique_joueur['HP'] += statistique_joueur['Soins']

            print("Ordinateur: Tu te soigne")
            print(f"\n\033[32m+{statistique_joueur['Soins']} HP\033[0m")    

        # Blocker
        if choix_attaque == '3':
            chance = random.choice([True,True,False])
            if chance:
                statistique_enemy["Puissance"] -= 5
        
        # Courrir
        elif choix_attaque == '4':
            courrir = random.choice([True,False])
            if courrir:
                print("\nOrdinateur: \033[32mTu t'es sauvé\033[0m")
                time.sleep(3)
                combat = False

            else:
                print("\nOrdinateur: \033[31mTu ne peut pas te sauver\033[0m")
                time.sleep(3)

        attaque_enemy = random.choice([True,True,False])

        if attaque_enemy:
            statistique_joueur["HP"] -= statistique_enemy["Puissance"]
            print(f"\nOuch!")
            print(f'\033[31m-{statistique_enemy["Puissance"]} HP\033[0m')
            print(f"Ordinateur: Il te reste {statistique_joueur['HP']} HP")
        
        else:
            print("\nWheh, il m'a preseque fait mal.")
            print(f'Ordinateur: Il te reste {statistique_joueur["HP"]} HP')

        if statistique_joueur["HP"] <= 0:
            return False

        if nombre_enemy <= 0:
            break
    print(f"\nOrdinateur: Bravo {nom_du_joueur}!\nOrdinateur: Tu as gagner un combat!")
    
    augmenter_niveau(statistique_joueur)
    
    return statistique_joueur
    


def afficher_statistique(statistique_joueur):
    print(f'HP: {statistique_joueur["HP"]}')
    print(f'Mana: {statistique_joueur["Mana"]}')
    print(f'Puissance: {statistique_joueur["Puissance"]}')
    print(f'Niveau: {statistique_joueur["Niveau"]}')
    print(f'EXP: {statistique_joueur["EXP"]}')
    print(f'Soins: {statistique_joueur["Soins"]}')


def augmenter(statistique_joueur):
    statistique_joueur["Puissance"] = statistique_joueur["Puissance"] + (statistique_joueur["Niveau"] * 5)
    statistique_joueur["HP"] = statistique_joueur["HP"] + (statistique_joueur["Niveau"] * 5)
    statistique_joueur["Soins"] = statistique_joueur["Soins"] + (statistique_joueur["Niveau"] * 2)
    statistique_joueur["Mana"] = statistique_joueur["Mana"] + (statistique_joueur["Niveau"] * 3)
    statistique_joueur["HP Base"] = statistique_joueur["HP"] + (statistique_joueur["Niveau"] * 5)


def augmenter_niveau(statistique_joueur):
    print("\nOrdinateur: Veut-tu voir tes statistiques?")
    affiche_statis_joueur = affichage_énnoncé('Oui','Non',None,None)

    if affiche_statis_joueur == '1':
    
        for i in range(10):

            if statistique_joueur["EXP"] >= 100 and statistique_joueur["Niveau"] == 1:
                statistique_joueur["Niveau"] = 2
                print(f"Ordinateur: \033[32mNiveau {statistique_joueur['Niveau']} déblocké \033[0m")
                statistique_joueur["HP"] = 100 
                augmenter(statistique_joueur)
            
            if statistique_joueur["EXP"] >= 500 and statistique_joueur["Niveau"] == 2:
                statistique_joueur["Niveau"] = 3
                print(f"Ordinateur: \033[32mNiveau {statistique_joueur['Niveau']} déblocké \033[0m")
                statistique_joueur["HP"] = 100
                augmenter(statistique_joueur)
            
            if statistique_joueur["EXP"] >= 1000 and statistique_joueur["Niveau"] == 3:
                statistique_joueur["Niveau"] = 4
                print(f"Ordinateur: \033[32mNiveau {statistique_joueur['Niveau']} déblocké \033[0m")
                statistique_joueur["HP"] = 100
                augmenter(statistique_joueur)    
            
            if statistique_joueur["EXP"] >= 1500 and statistique_joueur["Niveau"] == 4:
                statistique_joueur["Niveau"] = 5
                print(f"Ordinateur: \033[32mNiveau {statistique_joueur['Niveau']} déblocké \033[0m")
                statistique_joueur["HP"] = 100
                augmenter(statistique_joueur)    
            
            if statistique_joueur["EXP"] >= 2000 and statistique_joueur["Niveau"] == 5:
                statistique_joueur["Niveau"] = 6
                print(f"Ordinateur: \033[32mNiveau {statistique_joueur['Niveau']} déblocké \033[0m")
                statistique_joueur["HP"] = 100
                augmenter(statistique_joueur)    
            
            if statistique_joueur["EXP"] >= 2500 and statistique_joueur["Niveau"] == 6:
                statistique_joueur["Niveau"] = 7
                print(f"Ordinateur: \033[32mNiveau {statistique_joueur['Niveau']} déblocké \033[0m")
                statistique_joueur["HP"] = 100
                augmenter(statistique_joueur)
            
            if statistique_joueur["EXP"] >= 3000 and statistique_joueur["Niveau"] == 7:
                statistique_joueur["Niveau"] = 8
                print(f"Ordinateur: \033[32mNiveau {statistique_joueur['Niveau']} déblocké \033[0m")
                statistique_joueur["HP"] = 100
                augmenter(statistique_joueur)    
            
            if statistique_joueur["EXP"] >= 4000 and statistique_joueur["Niveau"] == 8:
                statistique_joueur["Niveau"] = 9
                print(f"Ordinateur: \033[32mNiveau {statistique_joueur['Niveau']} déblocké \033[0m")
                statistique_joueur["HP"] = 100
                augmenter(statistique_joueur)    
            
            if statistique_joueur["EXP"] >= 5000 and statistique_joueur["Niveau"] == 9:
                statistique_joueur["Niveau"] = 10
                print(f"Ordinateur: \033[32mNiveau {statistique_joueur['Niveau']} déblocké \033[0m")
                statistique_joueur["HP"] = 100
                augmenter(statistique_joueur)
    else:
        pass


def cut():
    time.sleep(10)
    system('cls')


def menu():
    print("Menu:")
    menu_choix = affichage_énnoncé('Mode: Survie', 'Mode: Histoire', 'Afficher les statistiques','Quitter')
    
    if menu_choix == '1':
        vague = 0
        nb_enemy = 1
        vie = combat(nb_enemy, class_du_joueur)
        
        while vie != False:
            
            vie = combat(nb_enemy, class_du_joueur)
            nb_enemy += random.randint(1,5)
            vague += 1

        print(f"\nTu as survécus {vague} vague(s)!\n")

        menu()

    elif menu_choix == '2':
        pass
    
    elif menu_choix == '3':
        afficher_statistique(statistique_joueur)
        menu()

    elif menu_choix == '4':
        fichiers = ['x1.txt','x2.txt','x3.txt']
        animation(fichiers, 0.3, 5)
        sauvgarder(nom_du_joueur, statistique_joueur)
        sys.exit()



def entrer(nom_du_joueur):
    # ICI
    os.chdir("C:\\Users\\aydip\\Projet informatique\\fichiers joueurs") # Lieu d'un fichier pour les comptes de joueurs

    print("Ordinateur: Veut tu login ou registrer?")
    enter_choice = affichage_énnoncé("Login","Registrer",None,None)

    if enter_choice == '2':
        deja_registrer = False
        fichier = open(f"{nom_du_joueur}.txt",'w')
        fichier.close()

    elif enter_choice == '1':
        deja_registrer = True
        try: 
            file = open(f"{nom_du_joueur}.txt", 'r')
            file.close()
        except:
            print("\nCompte pas trouver\n")
            entrer(nom_du_joueur)
    
    elif enter_choice != '1' and enter_choice != '2':
        entrer(nom_du_joueur)
    
    return deja_registrer


def sauvgarder(nom_du_joueur, statistique_joueur):
    fichier = open(f"{nom_du_joueur}.txt", 'w')
    fichier.write(f'{statistique_joueur["HP"]},{statistique_joueur["Mana"]},{statistique_joueur["Puissance"]},{statistique_joueur["Niveau"]},{statistique_joueur["EXP"]},{statistique_joueur["Soins"]},{statistique_joueur["HP Base"]},{class_du_joueur},{statistique_joueur["Defi"]}')
    fichier.close()


# +-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

print("""
REGLES:
1. Pour faire un choix, utilise les chiffres donné.
2. Chaque class à leur propre effets spéciaux
3. Amuse toi!!
""")

# Défi 1
time.sleep(5)

joueur = introduction()

deja_un_compte = joueur[1]
nom_du_joueur = joueur[0]

cut()

if not deja_un_compte:
    class_du_joueur = joueur[2]
    print("Bienvenue à ton premier combat! ")
    statistique_joueur = combat(2, class_du_joueur)
    statistique_joueur["Defi"] = 2

elif deja_un_compte:
    fichier = open(f"{nom_du_joueur}.txt",'r')
    statistique_joueur = fichier.read().split(',')

    class_du_joueur = statistique_joueur[7]

    statistique_joueur = {
    "HP": statistique_joueur[0],
    "Mana": statistique_joueur[1],
    "Puissance": statistique_joueur[2],
    "Niveau": statistique_joueur[3],
    "EXP": statistique_joueur[4],
    "Soins": statistique_joueur[5],
    "HP Base": statistique_joueur[6],
    "Defi": statistique_joueur[8]
    }
    afficher_statistique(statistique_joueur)


cut()


# Defi 2
if statistique_joueur["Defi"] == 2:
    menu()
    statistique_joueur["Defi"] = 3

# Defi 3
if statistique_joueur["Defi"] == 3:
    menu()
    # Histoire

    statistique_joueur["Defi"] = 4
# Etc...