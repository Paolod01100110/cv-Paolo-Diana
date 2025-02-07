class PersonaleCucina:
    def __init__(self, nome, eta):
        self.nome = nome #attributi di istanza
        self.eta = eta
    
    def lavora(self):
        print(f"{self.nome}, {self.eta} anni, sta lavorando in cucina.")

class Chef(PersonaleCucina):
    def __init__(self, nome, eta, specialita):
        super().__init__(nome, eta)
        self.specialita = specialita
    
    def lavora(self):
        print(f"{self.nome}, {self.eta} anni, è uno chef specializzato in {self.specialita}.")
    
    def prepara_menu(self):
        print(f"{self.nome} sta creando nuovi piatti e menu basati sulla cucina {self.specialita}.")

class SousChef(PersonaleCucina):
    def lavora(self):
        print(f"{self.nome}, {self.eta} anni, sta assistendo lo chef e gestendo l'inventario.")
    
    def gestisci_inventario(self):
        print(f"{self.nome} sta controllando e gestendo l'inventario della cucina.")

class CuocoLinea(PersonaleCucina):
    def lavora(self):
        print(f"{self.nome}, {self.eta} anni, sta cucinando i piatti sulla linea di produzione.")
    
    def cucina_piatto(self, nome_piatto):
        print(f"{self.nome} sta preparando il piatto: {nome_piatto}.")

# Esempio di utilizzo:
chef = Chef("Giorgio Locatelli", 50, "Cucina Italiana")
sous_chef = SousChef("Alessandro Rossi", 40)
cuoco_linea = CuocoLinea("Luca Bianchi", 30)

chef.lavora()
chef.prepara_menu()

sous_chef.lavora()
sous_chef.gestisci_inventario()

cuoco_linea.lavora()
cuoco_linea.cucina_piatto("Risotto alla Milanese")
