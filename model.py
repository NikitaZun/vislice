import random

STEVILO_DOVOLJENIH_NAPAK = 10
PRAVILNA_CRKA = '+'
PONOVLJENA_CRKA = 'o'
NAPACNA_CRKA = '-'
ZMAGA =  'W'
PORAZ = 'X'

class Igra:
    
    def __init__(self, geslo, crke=None):
        self.geslo = geslo
        if crke is None:
            self.crke = []
        else:
            self.crke = crke
        
    def napacne_crke(self):
        napacne_crke=[]
        for crka in self.crke:
            if crka not in self.geslo:
                napacne_crke.append(crka)
        return napacne_crke

    def pravilne_crke(self):
        pravilne_crke=[]
        for crka in self.crke:
            if crka in self.geslo:
                pravilne_crke.append(crka)
        return pravilne_crke

    def stevilo_napak(self):
        return len(self.napacne_crke())

    def zmaga(self):
        return all([crka in self.crke for crka in self.geslo])

    def poraz(self):
        return self.stevilo_napak() > STEVILO_DOVOLJENIH_NAPAK

    def pravilni_del_gesla(self):
        pravilni_del_gesla= ''
        for crka in self.geslo:
            if crka in self.crke:
                pravilni_del_gesla+= crka + ' '
            else:
                pravilni_del_gesla += ' _ '
        return pravilni_del_gesla

    def nepravilni_ugibi(self):
        return ' '.join(self.napacne_crke())

    def ugibaj(self,crka):
        crka = crka.upper()
        if crka in self.crke:
            return PONOVLJENA_CRKA
        else:
            self.crke.append(crka)
            if crka in self.geslo:
                if self.zmaga():
                    return ZMAGA
                else:
                    return PRAVILNA_CRKA
            else:
                if self.poraz():
                    return PORAZ
                else:
                    return NAPACNA_CRKA

with open('besede.txt', encoding='utf-8') as f:
    bazen_besed = [vrstica.strip().upper() for vrstica in f]

def nova_igra():
    return Igra(random.choice(bazen_besed))


