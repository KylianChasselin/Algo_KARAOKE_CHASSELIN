# CLASS ET DEF ----------------------------------------

class player: 
    def __init__(self, score, player, chanson):
        self.__score = 0
        self.__joueur = player
        self.__chanson = 4

    def getscore(self):
        return self.__score

    def getjoueur(self):
        return self.__joueur


class karaoke:
    def __init__(self, nom, chanson, score):
        self.__nomChanson = nom
        self.__scoreChanson = score
    
    def getscoreChanson(self):
        return self.__scoreChanson

    def getnomChanson(self) :
        return self.__nomChanson


# PROGRAMME PRINCIPAL ---------------------------------


nombreJoueur = input("combien de joueurs etes-vous ? -->  ")
joueur = player(nombreJoueur)
scoreMin = 50
scoreMax = 100
scoreObtenue = int(input("quel score avez-vous obtenue ? (minimum 50, max 100)"))
scoreTotal = 0
chanson = 0

while (scoreObtenue != scoreMax) : 
    if(scoreObtenue >= scoreMin):
        scoreTotal = scoreObtenue
    elif (scoreObtenue >= scoreMax) : 
        print("vous avez le score MAX ! --> ", scoreMax)
        scoreTotal = scoreTotal + scoreMax
    elif (scoreObtenue < scoreMin) :
        print("votre score n'est pas valable, veuillez entré de nouveau votre score")


#-------


choixChanson = int(input("choisissez votre chanson entre 1 et 5"))

chanson1 = karaoke ("venom",scoreTotal, 1)
chanson2 = karaoke ("Mayhem",scoreTotal, 2)
chanson3 = karaoke ("Looser",scoreTotal, 3)
chanson4 = karaoke ("My sanctuary",scoreTotal, 4)
chanson5 = karaoke ("Wap",scoreTotal, 5)

if choixChanson == 1 :
    print("vous avez choisi Venom, preparez vous a chanter")
    scorechanson1 = input("donnez votre score")
elif choixChanson == 2 :
    print("vous avez choisi Mayhem, preparez vous a chanter")
    scorechanson2 = input("donnez votre score")
elif choixChanson == 3 :
    print("vous avez choisi Looser, preparez vous a chanter")
    scorechanson3 = input("donnez votre score")
elif choixChanson == 4 :
    print("vous avez choisi My sanctuary, preparez vous a chanter")
    scorechanson4 = input("donnez votre score")
elif choixChanson == 5 :
    print("vous avez choisi Wap, preparez vous a chanter")
    scorechanson5 = input("donnez votre score")