# Les Sims facon COMMAND-LINE

"""Creation des meubles avec des Class:
CLASS FRIGO - action: manger, remplir
CLASS LIT - action: dormir
CLASS DOUCHE - action: se doucher
CLASS AMUSEMENT - action: regarder TV, lire un livre"""

class Frigo:

    def __init__(self):
        self.contenu = 5 # le frigo contient 5 plats au depart
        self.salete = 100


    def manger(self):
        print("Il y a {} plats dans le frigo.".format(self.contenu))
        input_manger = input("Voulez-vous manger? yes/no: ")

        if input_manger == 'yes':
            self.contenu -= 1
            self.salete -= 10
            print("Vous manger l'item!")
            sims.fatigue -= 4
            sims.faim += 20
            sims.hygiene -+ 9
            sims.distraction -= 5
        else:
            print("Vous avez changer d'avis.")
        
    def remplir(self):
        print("Vous allez faire les courses.")
        # Quand on ajoutera une variable MONEY:
        # print("Vous avez depenser {} Simflouzes et votyre frigo contient {} plats.".format(money, self.contenu))
        sims.fatigue -= 20
        self.contenu += 5
        sims.hygiene -= 10
        sims.distraction -= 35
        print("Vous avez maintenant {} plats dans votre frigo.".format(self.contenu))


    def nettoyer(self):
        print("Vous nettoyer le frigo!")
        self.salete = 100


# -------------------

class Lit:

    def __init__(self):
        self.salete = 100

    def dormir(self):
        se_coucher = input("Voulez vous vous coucher? yes/no : ")
        
        if se_coucher == 'yes':
            self.salete -= 15
            print("Vous vous enrouler sous la couette!")
            sims.fatigue = 99
            sims.hygiene -= 18
            sims.faim -= 40
            sims.distraction -= 20
        else:
            print("Vous avez changer d'avis.")


    def nettoyer(self):
        print("Vous nettoyer les draps du lit!")
        self.salete = 100


# -------------------

class Douche:

    def __init__(self):
        self.salete = 100

    def laver(self):
        se_laver = input("Voulez vous vous laver? yes/no : ")
        
        if se_laver == 'yes':
            self.salete -= 5
            print("Vous vous enfermez dans la douche!")
            sims.fatigue -= 9
            sims.faim -= 8
            sims.hygiene = 99
            sims.distraction -= 5
        else:
            print("Vous avez changer d'avis.")


    def nettoyer(self):
        print("Vous nettoyer la douche!")
        self.salete = 100


# -------------------

class Amusement:

    def watch(self):
        regarder_tv = input("Voulez vous regarder la TV? yes/no : ")
        
        if regarder_tv == 'yes':
            print("Vous vous abrutissez devant la television.")
            sims.fatigue -= 12
            sims.distraction += 30
            sims.hygiene -= 7
            sims.faim -= 6
        else:
            print("Vous avez changer d'avis.")
        
    def read(self):
        lire_livre = input("Voulez vous lire un livre? yes/no : ")
        if lire_livre == 'yes':
            print("Vous ouvrez un Shakespear.")
            sims.fatigue -= 10
            sims.distraction += 30
            sims.hygiene -= 4
            sims.faim -= 6
        else:
            print("Vous avez changer d'avis.")

# =======================================

"""Creation de la Class du Sims:
- Son nom
- Ses variables
- Son pognon (SOON)"""

class Personnage:

    def __init__(self, input_nom):
        self.nom = input_nom # pseudo du Sims

        # En dessous seront les variables jauges du Sims
        self.fatigue = 100
        self.faim = 100
        self.hygiene = 100
        self.distraction = 100


# =======================================
# =======================================


"""C'est ici que le programme va commencer. On initialize les variables de base.
On affiche un message de bienvenue au joueur et on prend le nom du Sims."""

print("Bienvenue sur les Sims Command-Line version!")

# Creation des meubles et du Sims:

nom_sims = input("Quel est le nom du Sims? ")
sims = Personnage(nom_sims)

frigo = Frigo()
lit = Lit()
douche = Douche()
amusement = Amusement()

# Contenu du jeu ici (PLATEAU)

game = True
while game == True:

    print("\nQue souhaitez-vous faire?\n"
          "1. Sims information\n"
          "2. Aller dans la cuisine\n"
          "3. Aller a la salle de bain\n"
          "4. Aller dans la chambre\n"
          "5. Aller dans le salon\n")

    choix = int(input("Entrer le nb correspondant a la piece: "))

    if choix == 1:
        print("\nNom du Sims: ", sims.nom)
        # indiquer au joueur depuis cb de temps il joue (cb de temps le program run)
        print("Faim: ", sims.faim, "\nFatigue: ", sims.fatigue, "\nHygiene: ", sims.hygiene, "\nAmusement: ", sims.distraction)

        # Happiness: moyenne des 4 autres variables vitales du Sims
        happiness = (sims.faim+sims.fatigue+sims.hygiene+sims.distraction)/4
        print("\nHappiness: ", happiness)


    if choix == 2:
        print("Ceci est la cuisine. Que faire?\n"
              "1. Se nourrir\n"
              "2. Faire les courses\n"
              "3. Nettoyer le frigo\n")
        choix2 = int(input("Entrer le nb de votre choix: "))

        if choix2 == 1:
            if frigo.salete <= 0:
                print("Desole mais le frigo pue, faut le laver.")
            else:
                frigo.manger()
        if choix2 == 2:
            frigo.remplir()
        if choix2 == 3:
            frigo.nettoyer()
        else:
            print("Choix non valide!")


    if choix == 3:
        print("Ceci est la salle de bain. Que faire?\n"
              "1. Se doucher\n"
              "2. Nettoyer la douche\n")
        choix2 = int(input("Entrer le nb de votre choix: "))

        if choix2 == 1:
            if douche.salete <= 0:
                print("Desole mais la douche est toute crade...")
            else:
                douche.laver()
        if choix2 == 2:
            douche.nettoyer()
        else:
            print("Choix non valide!")


    if choix == 4:
        print("Ceci est la chambre. Que faire?\n"
              "1. Se coucher\n"
              "2. Nettoyer les draps\n")
        choix2 = int(input("Entrer le nb de votre choix: "))

        if choix2 == 1:
            if lit.salete <= 0:
                print("Non, je dors pas dans des draps sales...")
            else:
                lit.dormir()
        if choix2 == 2:
            lit.nettoyer()
        else:
            print("Choix non valide!")


    if choix == 5:
        print("Ceci est le salon. Que faire?\n"
              "1. Regarder la Tv\n"
              "2. Lire un livre\n")
        choix2 = int(input("Entrer le nb de votre choix: "))

        if choix2 == 1:
            amusement.watch()
        if choix2 == 2:
            amusement.read()
        else:
            print("Choix non valide!")
