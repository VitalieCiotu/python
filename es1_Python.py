prezzi_prodotti = {
    ("Mela", "Lunedì", 1.0),
    ("Mela", "Martedì", 1.2),
    ("Mela", "Mercoledì", 1.1),
    ("Banana", "Lunedì", 0.8),
    ("Banana", "Martedì", 0.9),
    ("Banana", "Mercoledì", 0.7)
}

def prezzo_medio(prezzi_prodotti,product,gg):

    sommaM=0
    g=0
    for prodotto, giorno, prezzo in prezzi_prodotti:
        if prodotto == product:
            if giorno == gg:
                sommaM += prezzo
                g+=1
    M=sommaM/g
    return(M)


gg = input("Inserire il giorno: ")
product = input("Inserisci prodotto: ")
print(prezzo_medio(prezzi_prodotti,product,gg))

