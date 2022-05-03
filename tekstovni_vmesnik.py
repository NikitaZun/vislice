from model import PORAZ, STEVILO_DOVOLJENIH_NAPAK, ZMAGA, nova_igra


def izpis_igre(igra):
    return (
        '============================================================================\n' + 
        'Število preostalih poskusov: {}\n'.format(STEVILO_DOVOLJENIH_NAPAK - igra.stevilo_napak()) +
        'Pravilni del gesla: {}\n'.format(igra.pravilni_del_gesla()) +
        'Neuspeli poskusi: {}\n'.format(igra.nepravilni_del_gesla()) +
        '=========================================================================='
    )

def izpis_zmage(igra):
    return 'Čestitam. Uganil si geslo {}'.format(igra.geslo)

def izpis_poraza(igra):
    return 'Porabil si vse poskuse. Geslo je {}'.format(igra.geslo)

def zahtevaj_vnos():
    return input('Črka: ')

def pozeni_vmesnik():
    igra = nova_igra()
    while True:
        print(izpis_igre(igra))
        crka = zahtevaj_vnos()
        stanje = igra.ugibaj(crka)
        if stanje == ZMAGA:
            print(izpis_zmage(igra))
            break
        elif stanje == PORAZ:
            print(izpis_poraza(igra))
            break