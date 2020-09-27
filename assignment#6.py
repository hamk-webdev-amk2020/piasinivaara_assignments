# Ohjelma tarkistaa annetun henkilötunnuksen

from datetime import date
from datetime import datetime
import unicodedata

def tarkistusmerkki_OK(syntymaaika, yksilonumero, tarkistus):
    tarkistusmerkki = [
        '0','1','2','3','4','5','6','7','8','9',
        'A','B','C','D','E','F','H','J','K','L',
        'M','N','P','R','S','T','U','V','W','X','Y'
    ]
    
    jjaannos = int(syntymaaika + yksilonumero) % 31
    if not tarkistusmerkki[jjaannos] == tarkistus.upper():
        print ("Antamasi henkilötunnus on virheellinen. Tarkistusmerkki ei täsmää.")
        return False

    return True

def pvm_OK(pp, kk, vv):
    try :
        datetime(int(vv),int(kk),int(pp))
    except ValueError :
        print ("Annettu syntymäaika ei ole oikea pvm. Tarkista annettu hetu")
        return False
    else: return True

def valimerkki_OK(merkki):
    if merkki not in["A","-","+"]:
        print("Merkki syntymäajan jälkeen pitää olla 'A', '-' tai '+'")
        return False
    else: return True

def syntymaaika_OK(saika, merkki):
    
    if not saika.isnumeric(): 
        print ("Tarkista henkilötunnus, syntymäaikaosan pitää olla muotoa PPKKVV")
        return False
    #pilkotaan syntymäaika
    pp = saika[:2]
    kk = saika[2:4]
    vv = saika[4:6]

    # muutetaan syntymäajan vuosi muotoon vvvv ja tarkistetaan ettei vuosi ole tulevaisuudessa
    if valimerkki_OK(merkki):
        if merkki == "A": vvvv = int(vv) + 2000
        elif merkki == "-": vvvv = int(vv) + 1900
        else: vvvv = int(vv) + 1800
        today_vv = date.today().year
        if vvvv > today_vv: 
            print ("Korjaa henkilötunnus. Vuosi on tulevaisuudessa.")
            return False
    else: return False
   
    # tarkistetaan että henkilötunnuksen annettu päivämäärä on kelvollinen
    if not pvm_OK(pp,kk,vv): return False

    #palautetaan syntymäaika printattavassa muodossa
    output_hetu=str(pp)+'.'+str(kk)+'.'+str(vvvv)
    return (output_hetu)


def main():
    sotu2 = input("Anna henkilötunnus: ").strip()
    sotu=str(sotu2)
        
    if len(sotu) != 11: 
        print ("Annettu henkilötunnus on väärän mittainen.",len(sotu))
        return(0)
    #pilkotaan sotu osiin
    syntymaaika = sotu[:6]
    valimerkki = sotu[6]
    yksilonumero = sotu[7:10]
    sukupuoli = sotu[9:10]
    tarkistus = sotu[10:11]

    #tarkistetaan yksilönumeron oikeellisuus
    if not yksilonumero.isnumeric(): 
        print("Henkilötunnus on väärää muotoa. Välimerkin jälkeiset 3 merkkiä tulee olla numeroita.")
        return(0)

    #lasketaan onko tarkistumerkki ok
    if not tarkistusmerkki_OK(syntymaaika, yksilonumero, tarkistus): return(0)

    # tarkistetaan että annettu syntymäaika on oikeaa muotoa, tulostetaan syntymäaika
    saika=syntymaaika_OK(syntymaaika, valimerkki)
    if saika==False: return(0)
    else: print("Henkilötunnuksen omistajan syntymäaika on",saika)

    # tulostetaan henkilön sukupuoli
    jakojaannos = int(sukupuoli) % 2
    if jakojaannos==0: print("Henkilö on nainen")
    else: print("Henkilö on mies")




if __name__ == "__main__":
    main()