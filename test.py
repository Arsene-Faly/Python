class Personne:
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        
    def se_presenter(self):
        print(f"Bonjour {self.nom} {self.prenom}, vous êtes {self.age} ans")
        
    def est_majeur(self):
        return self.age > 18
    
class Employe(Personne):
    def __init__(self, nom, prenom, age, salaire):
        super().__init__(nom, prenom, age)
        self.salaire = salaire

    def se_presenter(self):
        print(f"Bonjour {self.nom} {self.prenom}, vous êtes {self.age} ans et votre salaire est {self.salaire}")
        
    # def est_majeur(self):
    #     return self.age > 18
    

P1 = Personne("Jean", "Dupont", 20)

E1 = Employe("Jean", "Dupont", 20, 1000)
E2 = Employe("Jean", "Dupont", 20, 1000)
E3 = Employe("Jean", "Dupont", 20, 1000)

for e in [E1, E2, E3]:
    e.se_presenter()
    
    if e.est_majeur():
        print("Vous êtes majeur")
    
    print()  # Ligne vide pour séparer chaque employé