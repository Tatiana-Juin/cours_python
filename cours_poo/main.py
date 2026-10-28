class Vehicule:
    def __init__(self,marque,modele,annee):
        # propriete
        self.marque = marque
        self.modele = modele
        self.annee = annee
    
    # methode
    def afficher(self):
        print(f"marque : {self.marque} le modele est : {self.modele} annee : {self.annee}")

class Moto(Vehicule):
    def __init__(self,marque,modele,annee,type_moto):
        # super execute le constructeur parent 
        super().__init__(marque,modele,annee)
        # self est une reference à l'instance de la classe 
        self.type_moto = type_moto
    
    def roue_arriere(self):
        print(f"La {self.modele} fait une roue arrière")

# class Voiture(Vehicule):
#     def __init__(self)
#----Creation d'un objet----
vehicule1 = Vehicule("Renault",'clio',2005)
# vehicule1.afficher()
ma_moto = Moto("Yamaha","MT-07",2021,"Roadster")
ma_moto.roue_arriere()
ma_moto.afficher()

