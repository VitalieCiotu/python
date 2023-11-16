tupla_pluviometrica = (
                      (("Vittuone","Milano"),(2022, ("gennaio",20))),
                      (("Vittuone","Milano"),(2023, ("marzo",80))),
                      (("Vittuone","Milano"),(2023, ("aprile",60))),
                      (("Vittuone","Milano"),(2023, ("maggio",80))),
                      (("Vittuone","Milano"),(2023, ("maggio",40))),
                      (("Vittuone","Milano"),(2023, ("luglio",30))),
                      (("Vittuone","Milano"),(2023, ("agosto","N/D"))),
                      (("Varenna","Lecco"),(2023, ("luglio",150))),
                      (("Morbegno","Sondrio"),(2023, ("luglio",165)))
                      )

def media_globale(tupla_pluviometrica):

    m=0
    i=0

    for provincia,dati in tupla_pluviometrica:
        for anno,altro in dati:
            for mese,mm in altro:
                if type(mm)==int:
                    m+=mm
                    i+=1
            media=m/i
            return (media)
        

def media(tupla_pluviometrica, provinciaB, meseB):
    x=0
    j=0
    for provincia,dati in tupla_pluviometrica:
        for citta,provinciaA in provincia:
           for anno,mese in dati:
                for meseA,mm in mese:
                  if provinciaA==provinciaB and meseA==meseB:
                       x+=mm
                       j+=1
        mediaM=x/j
        return(mediaM)

for i in range(99):
    print("1) quantitativo medio di pioggia rilevata nell'anno 2023")
    print("2) quantitativo medio di pioggia rilevata in una provincia in diversi mesi")
    print("3) il mese (o i mesi ) più piovoso/i della provincia di Milano")
    print("4) il mese con minor precipitazioni")
    print("5) percentuale delle precipitazioni per provincia rispetto al totale")

    scelta=int(input("\nInserisci scelta: "))

    if scelta==1:
        provinciaB=input("Inserisci provincia: ")
        meseB=input("Inserisci mese: ")
        print(media_globale(tupla_pluviometrica))
    if scelta==2:
        print(media(tupla_pluviometrica, provinciaB, meseB))
    if scelta==3:
    if scelta==4:
    if scelta==5: