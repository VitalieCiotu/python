prezzi_prodotti=(
    ("Mela",("Lunedi", 1.0), ("Martedi", 1.0), ("Mercoledi", 1.3), ("Giovedi", 1.5), ("Venerdi", 1.1), ("Sabato", 1.3)),
    ("Banana",("Lunedi", 1.1), ("Martedi", 1.3), ("Mercoledi", 1.3), ("Giovedi", 1.4), ("Venerdi", 1.5), ("Sabato", 1.6))
)

def prezzo_medio(prezzi_prodotti,product):       

    prezzoM=0
    g=0

    for prodotto, *altro in prezzi_prodotti:
        if prodotto==product:
            for giorno, prezzo in altro:
                prezzoM+=prezzo
                g+=1
            M=prezzoM/g
            return M
        
product=input("Inserisci prodotto: ")

print("Il prezzo medio del prodotto",product,"è di",prezzo_medio(prezzi_prodotti,product))

def prezzo_medioP(prezzo_medio):
    
    for prodotto, *altro in prezzi_prodotti:
        prezzoM=0
        g=0
        for giorno, prezzo in altro:
            prezzoM+=prezzo
            g+=1
        print("La media del prodotto",prodotto,"è di",prezzoM/g)

print("\nMedia tutti i prodotti:")
prezzo_medioP(prezzi_prodotti)

def prezzo_medioQ(prezzi_prodotti,product1):

    prezzoMax=0

    for prodotto, *altro in prezzi_prodotti:
        if prodotto==product:
            for giorno, prezzo in altro:
                if prezzoMax<prezzo:
                    prezzoMax=prezzo
            print("Il prezzo massimo è di:",prezzoMax)
            for giorno, prezzo in altro:
                if prezzoMax==prezzo:
                    print("Nel giorno:",giorno)

print("\nPrezzo massimo prodotto e giorni in cui si verifica:")
product1=input("Inserisci prodotto:")
prezzo_medioQ(prezzi_prodotti, product1)