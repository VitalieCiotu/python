risultatiCampionati={}

def popola(risultatiCampionati):
  Gullo={"Giuseppe Gullo":[(40,21,0),"junior mas", (0,12,0),"junior mas", (0,29,19),"junior mas"]}
  Barbera={"Antonio Barbera":[(0,39,11),"junior fem", (0,18,0),"junior fem", (0,0,0),"junior fem"]}
  Esposito={"Nicola Esposito":[(0,43,22),"junior mas", (0,14,0),"junior mas", (0,36,19),"junior mas"]}
         
  risultatiCampionati.update(Gullo)
  risultatiCampionati.update(Barbera)
  risultatiCampionati.update(Esposito)  

  print("Dizzionario POPOLATO!!!")

def popolaMe(risultatiCampionati):
  nome=input("Inserisci nome: ")
  while nome=="":
    nome=input("Reinserisci nome: ")

  min=0

  sec=4

  cent=0

  categoria=input("Inserisci categoria: ")
  while categoria=="":
    categoria=input("Reinserisci categoria: ")

  risultatiNome={nome:[(min,sec,cent),categoria,(min,sec,cent),categoria,(min,sec,cent),categoria]}
  risultatiCampionati.update(risultatiNome)


def nuovaDisciplina(risultatiCampionati):
  for chiave,valori in risultatiCampionati.items():
    if(chiave=='Giuseppe Gullo'):
      valori.append(((9,5,0),"senior mef"))
    elif(chiave=='Antonio Barbera'):
      valori.append(((14,0,4),"senior fem"))
    elif(chiave=='Nicola Esposito'):
      valori.append(((6,12,1),"senior fem"))

  print(risultatiCampionati)
    

def stampaGullo(risultatiCampionati,o):
  for chiave,valori in risultatiCampionati.items():
    if(chiave=='Giuseppe Gullo'):
      if(o==0):
        print("Nome:",chiave,"  tempi campestre:",valori[0]," categoria:",valori[1]," tempi 100m:", valori[2], " categoria:", valori[3], " tempi 200m:",valori[4])
      else:
        print("Nome:",chiave,"  tempi campestre:",valori[0]," categoria:",valori[1]," tempi 100m:", valori[2], " categoria:", valori[3], " tempi 200m:",valori[4], " tempi 400m", valori[5], " categoria:",valori[6]) 


def stampaNicola(risultatiCampionati):
  for chiave,valori in risultatiCampionati.items():
    if(chiave=='Nicola Esposito'):
      print("Nome: ",chiave, " tempi 200m:","( min:",valori[4][0],"sec:",valori[4][1]," cent:", valori[4][2],")")


def stampaBarbera(risultatiCampionati):
  for chiave,valori in risultatiCampionati.items():
    if(chiave=='Antonio Barbera'):
      print("Nome: ",chiave, " tempi 100m:","( min:",valori[2][0],"sec:",valori[2][1]," cent:", valori[2][2],")")


def tempoMax(risultatiCampionati):
  tempi=[]
  for chiave, valori in risultatiCampionati.items():
    if valori[5]=="junior mas":
      tempi.append(valori[4])

  maxTempo=max(tempi)
  print("Tempo massimo 200m: ",maxTempo)


def tempoMin(risultatiCampionati):
  tempi=[]
  studente=""

  for chiave, valori in risultatiCampionati.items():
    if valori[5]=="junior mas":
      tempi.append(valori[2])

  minTempo=min(tempi)

  for chiave, valori in risultatiCampionati.items():
    if valori[2]==minTempo:
      studente=chiave

  print("Tempo minimo 100m: ",minTempo, " eseguito da:",studente)


def mediaTempi(risultatiCampionati):
  tempiMin=0
  tempiSec=0
  tempiCent=0
  i=0

  for chiave, valore in risultatiCampionati.items():
    tempiMin+=valore[0][0]
    tempiSec+=valore[0][1]
    tempiCent+=valore[0][2]
    i+=1

  print("Media tempi corsa campestre: ", "min",round((tempiMin/i),2), "sec: ",round((tempiSec/i), 2), " cent:",round((tempiCent/i), 2))


def nuovoMembro(risultatiCampionati):
  nuovoMembro={}
  if(o==0):
    nome=input("Inserisci nome: ")
    while nome=="":
      nome=input("Reinserisci nome: ")

    categoria=input("Inserisci categoria: ")
    while categoria=="":
      categoria=input("Reinserisci categoria: ")

    minC=int(input("Inserisci minuti campestre:"))
    while(minC<0):
      minC=int(input("Reinserisci minuti campestre:"))
    
    secC=int(input("Inserisci secondi campestre:"))
    while(secC<0):
      secC=int(input("Reinserisci secondi campestre:"))

    centC=int(input("Inserisci centesimi campestre:"))
    while(centC<0):
      secC=int(input("Reinserisci centesimi campestre:"))

    min100=int(input("Inserisci minuti corsa 100m:"))
    while(min100<0):
      min100=int(input("Reinserisci minuti corsa 100m:"))
    
    sec100=int(input("Inserisci secondi corsa 100m:"))
    while(sec100<0):
     sec100=int(input("Reinserisci secondi corsa 100m:"))

    cent100=int(input("Inserisci centesimi corsa 100m:"))
    while(cent100<0):
      sec100=int(input("Reinserisci centesimi corsa 100m:"))

    min200=int(input("Inserisci minuti corsa 200m:"))
    while(min200<0):
      min200=int(input("Reinserisci minuti corsa 200m:"))
    
    sec200=int(input("Inserisci secondi corsa 200m:"))
    while(sec200<0):
      sec200=int(input("Reinserisci secondi corsa 200m:"))

    cent200=int(input("Inserisci centesimi corsa 200m:"))
    while(cent200<0):
      sec200=int(input("Reinserisci centesimi corsa 200m:"))

    nuovoMembro={nome:[(minC,secC,centC),categoria,(min100,sec100,cent100),categoria,(min200,sec200,cent200),categoria]}
    risultatiCampionati.update(nuovoMembro)
  else:

    nome=input("Inserisci nome: ")
    while nome=="":
      nome=input("Reinserisci nome: ")

    categoria=input("Inserisci categoria: ")
    while categoria=="":
      categoria=input("Reinserisci categoria: ")

    minC=int(input("Inserisci minuti campestre:"))
    while(minC<0):
      minC=int(input("Reinserisci minuti campestre:"))
    
    secC=int(input("Inserisci secondi campestre:"))
    while(secC<0):
      secC=int(input("Reinserisci secondi campestre:"))

    centC=int(input("Inserisci centesimi campestre:"))
    while(centC<0):
      secC=int(input("Reinserisci centesimi campestre:"))

    min100=int(input("Inserisci minuti corsa 100m:"))
    while(min100<0):
      min100=int(input("Reinserisci minuti corsa 100m:"))
    
    sec100=int(input("Inserisci secondi corsa 100m:"))
    while(sec100<0):
     sec100=int(input("Reinserisci secondi corsa 100m:"))

    cent100=int(input("Inserisci centesimi corsa 100m:"))
    while(cent100<0):
      sec100=int(input("Reinserisci centesimi corsa 100m:"))

    min200=int(input("Inserisci minuti corsa 200m:"))
    while(min200<0):
      min200=int(input("Reinserisci minuti corsa 200m:"))
    
    sec200=int(input("Inserisci secondi corsa 200m:"))
    while(sec200<0):
      sec200=int(input("Reinserisci secondi corsa 200m:"))

    cent200=int(input("Inserisci centesimi corsa 200m:"))
    while(cent200<0):
      sec200=int(input("Reinserisci centesimi corsa 200m:"))

    min400=int(input("Inserisci minuti corsa 400m:"))
    while(min400<0):
      min400=int(input("Reinserisci minuti corsa 400m:"))
    
    sec400=int(input("Inserisci secondi corsa 400m:"))
    while(sec400<0):
      sec400=int(input("Reinserisci secondi corsa 400m:"))

    cent400=int(input("Inserisci centesimi corsa 400m:"))
    while(cent400<0):
      sec400=int(input("Reinserisci centesimi corsa 400m:"))

  nuovoMembro={nome:[(minC,secC,centC),categoria,(min100,sec100,cent100),categoria,(min200,sec200,cent200),categoria,(min400,sec400,cent400),categoria]}
  risultatiCampionati.update(nuovoMembro)


o=0
scelta=0
while True:
  print()
  print("1. Popola il dizionario con i dati qui sopra")
  print("2. Aggiungi alla struttura il tuo nominativo con valori a scelta, tranne il numero di secondi che deve essere (N il tuo numero di registro)")
  print("3. Aggiungi la 4.disciplina sportiva 'corsa ad ostacoli 400 mt' per ogni atleta con la relativa categoria e tempi a tua scelta")
  print("4. Stampa la tupla con le informazioni sulla disciplina sportiva corsa campestre per l'atleta Giuseppe Gullo")
  print("5. Stampa i singoli valori della tupla con le informazioni sulla disciplina corsa 200 mt. per Nicola Esposito")
  print("6. Stampa il tempo di Antonia Barbera nella corsa 100 mt separando min,sec,cent")
  print("7. Stampa il tempo massimo riportato nella corsa 200mt della categoria Juniores mas (guarda l'aiuto)")
  print("8. Stampa il tempo minimo riportato nella corsa 100mt. della categoria Juniores mas. e lo studente che lo ha realizzato")
  print("9. Stampa la media dei tempi nella corsa campestre della categoria Juniores mas")
  print("10. Realizzare le opportune funzioni per aggiungere al dizionario i dati validi relativi alle 4 gare per un nuovo atleta")
  print("0. EXIT")
  scelta=int(input(":"))

  if scelta==0:
    print("FINITO!!!")
    break

  if scelta==1:
    popola(risultatiCampionati)
  
  if scelta==2:
    popolaMe(risultatiCampionati)

  if scelta==3:
    nuovaDisciplina(risultatiCampionati)
    o+=1

  if scelta==4:
    stampaGullo(risultatiCampionati,o)

  if scelta==5:
    stampaNicola(risultatiCampionati)

  if scelta==6:
    stampaBarbera(risultatiCampionati)

  if scelta==7:
    tempoMax(risultatiCampionati)

  if scelta==8:
    tempoMin(risultatiCampionati)

  if scelta==9:
    mediaTempi(risultatiCampionati)

  if scelta==10:
    nuovoMembro(risultatiCampionati)
