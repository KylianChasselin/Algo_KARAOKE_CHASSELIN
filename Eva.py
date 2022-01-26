# CLASS ET DEF ----------------------------------------

class player: 
    def __init__(self, score, player, chanson):
        self.__score = 0
        self.__joueur = player
        self.__chanson = 4

    def getscoreJoueur(self):
        return self.__score

    def getplayer(self):
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

chanson1 = karaoke ("venom",scoreTotal, 1)
chanson2 = karaoke ("",scoreTotal, 2)
chanson3 = karaoke ("",scoreTotal, 3)
chanson4 = karaoke ("",scoreTotal, 4)
chanson5 = karaoke ("",scoreTotal, 5)