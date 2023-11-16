dati_vendite=(
    ("cucina", [("gennaio", "N/D"),("febraio", 450),("marzo", 700),("aprile", 600),("maggio", 750),("giugno", "N/D"),("luglio", 350),("agosto", 200),("settembre", 350),("ottobre", 450),("novembre", 600),("dicembre", 700),]),
    ("bagno", [("gennaio", 350),("febraio", 750),("marzo", 200),("aprile", "N/D"),("maggio", 150),("giugno", 200),("luglio", "N/D"),("agosto", 200),("settembre", 300),("ottobre", 100),("novembre", 200),("dicembre", 600),]),
    ("salotto", [("gennaio", 900),("febraio", "N/D"),("marzo", 450),("aprile", "N/D"),("maggio", 750),("giugno", 400),("luglio", 300),("agosto", 250),("settembre", 100),("ottobre", 1000),("novembre", 350),("dicembre", 800),])
    )

def media_vendite(nome_reparto, dati_vendite):
    
    m=0
    i=0
    max=0
    min=9999999
    j=0
    mesi_max=[]
    mesi_min=[]

    for reparto,vendite in dati_vendite:
        if reparto==nome_reparto:
            for mese, importo in vendite:
                if type(importo)==int:
                    m+=importo
                    i+=1
                    if importo>max:
                        max=importo
                    if importo<min:
                        min=importo
            for mese, importo in vendite:
                    if importo==max:
                        mesi_max.append(mese)
                    if importo==min:
                        mesi_min.append(mese)
                        
            media=m/i
            return(media,max,mesi_max,min,mesi_min)
            

nome_reparto=input("Inserisci nome reparto: ")

print(media_vendite(nome_reparto,dati_vendite))