# interface du jeu :
def morpion():
    cases = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    def afficher():
        n = 0
        for i in range(3):
            print(f" {cases[n]} | {cases[n+1]} | {cases[n+2]} ")
            if i < 2:
                print("---+---+---")
            n += 3

    afficher()

    # on répète 9 tours maximum
    for tour in range(9):
        if tour % 2 == 0:
            symbole = "X"
            joueur = 1
        else:
            symbole = "O"
            joueur = 2

        choix = int(input(f"Joueur {joueur} ({symbole}), choisis un chiffre : "))

        # si la case est déjà prise
        if cases[choix - 1] in ["X", "O"]:
            print("Case déjà prise, choisis-en une autre.")
            continue

        cases[choix - 1] = symbole
        afficher()

    print("Fin de la partie !")

morpion()
