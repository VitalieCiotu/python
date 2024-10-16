class Persona:
    def __init__(self, nome, cognome, codice_fiscale):
       self.nome=nome
       self.cognome=cognome
       self.codice_fiscale=codice_fiscale

class Socio(Persona):
    def __init__(self, nome, cognome, codice_fiscale, durata_iscrizione):
        super().__init__(nome, cognome, codice_fiscale)
        self.durata_iscrizione=durata_iscrizione

class Sede:
    def __init__(self, nome, indirizzo, max_soci, max_corsi):
        self.nome=nome
        self.indirizzo=indirizzo
        self.max_soci=max_soci
        self.max_corsi=max_corsi
        self.corsi=[]
        self.soci=[]

    def aggiungi_socio(self, socio):
        if len(self.soci) < self.max_soci:
            self.soci.append(socio)
        else:
            print("La sede è piena.")

    def numero_soci(self):
      return len(self.soci)

    def incasso_previsto(self, quota_mensile):
        return self.numero_soci()*quota_mensile

    def aggiungi_corso(self, corso):
        if self.max_corsi>len(self.corsi):
          self.corsi.append(corso)
        else:
          print("troppi corsi già attivi")

    def numero_corsi(self):
      return len(self.corsi)

    def incasso_corsi(self):
      for corso in self.corsi():
        tot+=len(corso.partecipanti)*corso.costo_partecipazione
      if tot==0:
        print("il corso non possiede partecipanti")
      else:
        return tot


class Palestra:
    def __init__(self):
        self.sedi=[]

    def aggiungi_sede(self, sede):
        self.sedi.append(sede)

    def numero_totale_soci(self):
        tot=0
        for sede in self.sedi:
            tot+=sede.numero_soci()
        if tot==0:
          print("non sono presenti soci")
        else:
          return tot

    def incasso_totale(self, quota_mensile):
      mesi=0
      for sede in self.sedi:
        for socio in sede.soci:
          mesi+=socio.durata_iscrizione

      if mesi==0:
        print("non sono presenti soci")
      else:
        return mesi*quota_mensile

    def aggiungi_corso(self, sede, corso):
      presente=sede in self.sedi
      if presente:
        sede.aggiungi_corso(corso)
        print("corso aggiunto con successo")
      else:
        print("errore sede inesistente")



