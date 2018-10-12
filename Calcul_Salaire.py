# coding: utf-8

def CalculSalaire(metier, experience):
    if metier == "Architecte" and experience == 4 :
        return "4000"
    elif metier == "Médecin" and experience == 8 :
        return "7000"
    elif metier == "Consultant" and experience == 5 :
        return "5000"

print ("Vous êtes {0}. Vous avez {1} ans d'expérience. Vous gagnez donc {2} euros.".format("Architecte", 4, "4000"))
print ("Vous êtes {0}. Vous avez {1} ans d'expérience. Vous gagnez donc {2} euros.".format("Médecin", 8, "7000"))
print ("Vous êtes {0}. Vous avez {1} ans d'expérience. Vous gagnez donc {2} euros.".format("Consultant", 5, "5000"))