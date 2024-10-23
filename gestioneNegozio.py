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
          print("Codice Modificato Con Successo!!!")

        case 2:
          fornitoreN = input("Inserisci Nuovo Fornitore: ")
          while fornitoreN == " ":
            fornitoreN = input("Reinsericsi nuovo fornitore: ")
          
          self.fornitore = fornitoreN
          print("Fornitore Modificato Con Successo!!!")

        case 3:
          marcaN = input("Inserisci nuova marca: ")
          while marcaN==" ":
            marcaN = input("Reinserisci nuova marca: ")
          
          self.marca = marcaN
          print("Marca Modificata Con Successo!!!")

        case 4:
          prezzoN = int(input("Inserisci Nuovo Prezzo: "))
          while prezzoN<0:
            prezzoN = int(input("Reinserisci Nuovo Prezzo: "))
          
          self.prezzo = prezzoN
          print("Prezzo Modificato Con Successo!!!")

        case 5:
          quantitaN = int(input("Inserisci Nuova Qauntita: "))
          while quantitaN<0:
            quantitaN = int(input("Reinserisci Nuova Quantita: "))

          self.quantita = quantitaN
          print("Quantita Modificato Con Successo!!!")
          
        case _:
          print("Inserire scelta tra quelle proposte!!!")


class Televisore(Articolo):#09:48
    def __init__(self, codice, fornitore,marca,prezzo,quantita,pollici,tipo):
      super().__init__(codice, fornitore, marca, prezzo, quantita)
      self.pollici = pollici
      self.tipo = tipo

    def scheda_articolo(self):
      return (f"{super().scheda_articolo()} \nPollici:  {self.pollici} \nTipo:  {self.tipo}")
    

class Frigorifero(Articolo):#09:48
  def __init__(self, codice, fornitore, marca, prezzo, quantita,dimensioni,modello):
    super().__init__(codice, fornitore, marca, prezzo, quantita)
    self.dimensioni = dimensioni
    self.modello = modello

  def scheda_articolo(self):
    return(f"{super().scheda_articolo()} \nDimensioni:  {self.dimensioni} \nModello:  {self.modello}")



#t1 = Televisore(1,"Fornitore 1","Sony",700, 10, 40,"Schermo piatto")
#print(t1.scheda_articolo())

#t1.modifica_scheda()
#print(t1.scheda_articolo())



class Ordine():#10:27
  def __init__(self, codice, data, piva, indirizzo):
    self.codice = codice
    self.data = data
    self.piva = piva
    self.indirizzo = indirizzo
    self.lista_articoli = [] 

  def aggiungi_articolo(self,articolo):
    if isinstance(articolo,Televisore):
      self.tipo_articolo="Televisore"
    elif isinstance(articolo,Frigorifero):
      self.tipo_articolo="Frigorifero"

    self.lista_articoli.append(articolo)
    print(f"{self.tipo_articolo} aggiunto con succsesso all'ordine {self.codice}!")

  def rimuovi_articolo(self,articolo):
    if articolo in self.lista_articoli:
      self.lista_articoli.remove(articolo)
      print(f"{self.tipo_articolo} con codice {articolo.codice} Rimosso Con Successo!!!")
    else:
      print(f"{self.tipo_articolo} con codice {articolo.codice} Non Presente!!!")

  def importo_ordine(self):
    numero_articoli = len(self.lista_articoli)
    importo_totale = sum(articolo.prezzo for articolo in self.lista_articoli) #Prende il prezzo di ogni articolo presente nella lista_articoli

    print(f"Importo Ordine Con Codice: ({self.codice}) Contenente ({numero_articoli}) Articoli = {importo_totale}")

  def dettaglio_ordine(self):
    sommaT = sum(articolo.prezzo for articolo in self.lista_articoli if isinstance(articolo, Televisore))#Prende il prezzo di ogni articolo presente nella lista_articoli e controlla se fa parte della classe Televisore/Frigorifero
    sommaF = sum(articolo.prezzo for articolo in self.lista_articoli if isinstance(articolo, Frigorifero))

    for articolo in self.lista_articoli:
     
      if isinstance(articolo, Televisore):
        print(f"\nArticolo: {"Televisore"} \n\tCodice: {articolo.codice} \n\tFornitore: {articolo.fornitore}  \n\tMarca: {articolo.marca} \n\tPrezzo: {articolo.prezzo} \n\tQuantità: {articolo.quantita}")
        print(f"\n\t\tPollici: {articolo.pollici} \n\t\tTipo: {articolo.tipo}")
        
      elif isinstance(articolo, Frigorifero):
        print(f"\nArticolo: {"Frigorifero"} \n\tCodice: {articolo.codice} \n\tFornitore: {articolo.fornitore}  \n\tMarca: {articolo.marca} \n\tPrezzo: {articolo.prezzo} \n\tQuantità: {articolo.quantita}")
        print(f"\n\t\tDimensioni: {articolo.dimensioni} \n\t\tModello: {articolo.modello}")
        
    
    return([sommaT, sommaF, sommaT+sommaF])



#t2 = Televisore(2,"Fornitore 2","Samsung",1000,5,80,"Schermo curvo")
#f1 = Frigorifero(3,"Fornitore 3","Bosch",750,12,'790x2000x600','Ultra')
#f2 = Frigorifero(4,"Fornitore 4","Ariston",550,10,'590x1600x500','Medium')


#ordine1=Ordine(1,"24/02/2022",'213143','Via della consegna 1')
#ordine1.aggiungi_articolo(t1)
#ordine1.aggiungi_articolo(t2)
#ordine1.aggiungi_articolo(f1)
#ordine1.aggiungi_articolo(f2)


#ordine1.rimuovi_articolo(f2)
#ordine1.rimuovi_articolo(f2)


#ordine1.importo_ordine()


#importi=ordine1.dettaglio_ordine()
#print("--------------------------")
#print(f"\nImporto televisori= {importi[0]}")
#print(f"\nImporto frigoriferi= {importi[1]}")
#print(f"\nImporto totale= {importi[2]}")



class Ordini():#10:57
  def __init__(self,nome_negozio,codice_negozio):
    self.nome_negozio = nome_negozio
    self.codice_negozio = codice_negozio
    self.lista_ordini = []

  def aggiungi_ordine(self,ordine):
    self.lista_ordini.append(ordine)
    print(f"Ordine Numero: ({ordine.codice}) Aggiunto Con Successo Alla Lista!")

  def rimuovi_ordine(self,ordine):
    if ordine in self.lista_ordini:
      self.lista_ordini.remove(ordine)
      print(f"Ordine Numero: ({ordine.codice}) Rimosso Con Successo Dalla Lista!")
    else:
      print(f"Vendita numero: ({ordine.codice}) Non Presente Nella Lista!")

  def totale_ordini(self):
    totT = 0
    totF = 0
    tot = 0

    for ordine in self.lista_ordini:
      dettaglio = ordine.dettaglio_ordine()
      totT += dettaglio[0]
      totF += dettaglio[1]

    tot = totF + totT

    return ([totT, totF, tot])



#ordini_negozio=Ordini("Megastore vendita ",1)
#ordini_negozio.aggiungi_ordine(ordine1)
#ordini_negozio.rimuovi_ordine(ordine1)
#ordini_negozio.rimuovi_ordine(ordine1)


#ordini_negozio.aggiungi_ordine(ordine1)


#t3 = Televisore(5,"Fornitore 5","LG",600,4,70,"Schermo curvo")
#f3 = Frigorifero(6,"Fornitore 6","Bosch",450,10,'490x1000x400','Small')
#ordine2=Ordine(2,"25/02/2022",'213113','Via della consegna 2')
#ordine2.aggiungi_articolo(t3)
#ordine2.aggiungi_articolo(f3)


#ordini_negozio.aggiungi_ordine(ordine2)


#importiTotali=ordini_negozio.totale_ordini()
#print("--------------------------")
#print(f"\nImporto totale televisori= {importiTotali[0]}")
#print(f"\nImporto totale frigoriferi= {importiTotali[1]}")
#print(f"\nImporto totale tutti gli ordini= {importiTotali[2]}")