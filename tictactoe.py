def morpion():
    #creation des cases
    cases = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    #fonction qui affiche la grille
    def afficher():
        n = 0
        for i in range(3): #3 lignes
            print(f" {cases[n]} | {cases[n+1]} | {cases[n+2]} ")
            if i < 2: #ne pas mettre de ligne de separation apres la derniere
                print("---+---+---")
            n += 3

    def gagnant():
        lignes = [
            (0,1,2), (3,4,5), (6,7,8),       # horizontales
            (0,3,6), (1,4,7), (2,5,8),       # verticales
            (0,4,8), (2,4,6)                 # diagonales
        ]
        for a, b, c in lignes:
            if cases[a] == cases[b] == cases[c] and cases[a] in ["X", "O"]:
                return cases[a]
        return ""
    
    #affichage initial du jeu
    afficher()

    #boucle 9 tours maximum
    for tour in range(9):
        #choix du joueur suivant le numero du tour
        if tour % 2 == 0:
            symbole = "X"
            joueur = 1
        else:
            symbole = "O"
            joueur = 2

        choix = 0
        #tant que la case est deja prise ou ne corrrespond pas a la grille, on redemande au meme joueur
        while choix not in range(1, 10) or cases[choix - 1] in ["X", "O"]:
            choix = int(input(f"Joueur {joueur} ({symbole}), choisis un chiffre : "))
            
            if choix not in range(1, 10):
                print("numero de case invalide, choisis entre 1 et 9.")
                continue
            if cases[choix - 1] in ["X", "O"]:
                print("Case déjà prise, recommence.")
                continue

        #mise a jour de la grille
        cases[choix - 1] = symbole
        #affichage apres chaque coup
        afficher()

        v = gagnant()
        if v != "":
            print(f"Joueur {joueur} ({v}) a gagné !")
            return
    print("Fin de la partie.")
    print("Match nul, personne n'a gagné.")

morpion()
