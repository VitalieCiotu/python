class Articolo:#09/40
  def __init__(self, codice, fornitore, marca, prezzo, quantita):
    self.codice = codice
    self.fornitore = fornitore
    self.marca = marca
    self.prezzo = prezzo
    self.quantita = quantita


  def scheda_articolo(self):
    return (f"\nCodice: {self.codice} \nFornitore:  {self.fornitore} \nMarca: {self.marca} \nPrezzo:  {self.prezzo} \nQuantita: {self.quantita}")


  def modifica_scheda(self):
    while True:
      print("1. Modifica Codice") 
      print("2. Modifica Fornitore")
      print("3. Modifica Marca")
      print("4. Modifica Prezzo")
      print("5. Modifica Quantita")
      print("0. EXIT")
      s=int(input(": "))

      match(s):
        case 0:
          break
        
        case 1:
          codiceN = input("Inserisci Nuovo Codice: ")
          while len(codiceN) != 4:
            codiceN = input("Reinserisci Nuovo Codice (4 cifre): ")

          self.codice = int(codiceN)

        case 2:
          fornitoreN = input("Inserisci Nuovo Fornitore: ")
          while fornitoreN == " ":
            fornitoreN = input("Reinsericsi nuovo fornitore: ")
          
          self.fornitore = fornitoreN

        case 3:
          marcaN = input("Inserisci nuova marca: ")
          while marcaN==" ":
            marcaN = input("Reinserisci nuova marca: ")
          
          self.marca = marcaN

        case 4:
          prezzoN = int(input("Inserisci Nuovo Prezzo: "))
          while prezzoN<0:
            prezzoN = int(input("Reinserisci Nuovo Prezzo: "))
          
          self.prezzo = prezzoN

        case 5:
          quantitaN = int(input("Inserisci Nuova Qauntita: "))
          while quantitaN<0:
            quantitaN = int(input("Reinserisci Nuova Quantita: "))

          self.quantita = quantitaN

        case _:
          print("Inserire scelta tra quelle proposte!!!")


class Televisore(Articolo):
    def __init__(self, codice, fornitore,marca,prezzo,quantita,pollici,tipo):
      super().__init__(codice, fornitore, marca, prezzo, quantita)
      self.pollici = pollici
      self.tipo = tipo

    def scheda_articolo(self):
      return (f"{super().scheda_articolo()} \nPollici:  {self.pollici} \nTipo:  {self.tipo}")
    

t1 = Televisore(1,"Fornitore 1","Sony",700, 10, 40,"Schermo piatto")
print(t1.scheda_articolo())

t1.modifica_scheda()
print(t1.scheda_articolo())