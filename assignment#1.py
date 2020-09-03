import json
from copy import deepcopy

def valikko():
    print ("\nSanakirja: ")
    print ("(1) Etsi sana sanakirjasta ")
    print ("(2) Näytä sanakirjan sisältö ")
    print ("(3) Poistu ohjelmasta")
    toiminto = input("Valitse toiminto: ")
    return toiminto.strip()

def sanakirjan_alustus():
    data = {}
    data['sanat'] = []
    data['sanat'].append({
    'sana': 'kissa',
    'selitys': 'Kotieläin'
    })
    data['sanat'].append({
    'sana': 'koira',
    'selitys': 'Kuolaava kotieläin'
    })
    data['sanat'].append({
    'sana': 'aasi',
    'selitys': 'Puhin kaveri'
    })

    sorted_data = deepcopy(data)
    sorted_data['sanat'] = sorted(data['sanat'], key=lambda k: k['sana'], reverse=False)

    with open('sanakirja.json', 'w') as tiedosto:
        json.dump(sorted_data, tiedosto)
    
    tiedosto.close()

def main():
    try:
        tiedosto=open("sanakirja.json","r")
        tiedosto.close()
    except Exception:
        sanakirjan_alustus()

    while True:

        valinta=valikko()

#   tulostetaan sanakirjan sisältö
        if valinta=="2":
            print("Sanakirjan sisältö on:\n")
            with open('sanakirja.json') as tiedosto:
                rivit = json.load(tiedosto)
                for i in rivit['sanat']:
                    print('Sana:    ' + i['sana'])
                    print('Selitys: ' + i['selitys'])
                    print('')
            tiedosto.close()

# poistutaan sanakirjasta
        elif valinta=="3": 
            print("Poistuit sanakirjasta. Tervetuloa uudelleen!")
            break
# haetaan hakusanalla - lisätään uusi hakusana jos käyttäjä haluaa
        elif valinta=="1":
            hakusana=input("Anna hakusana: ").lower().strip()
            with open('sanakirja.json') as tiedosto:
                rivit = json.load(tiedosto)
                loytyiko=False
                for i in rivit['sanat']:
                    if i['sana']==hakusana:
                        loytyiko=True
                        print('Sana löytyi sanakirjasta:')
                        print(hakusana,':',i['selitys'])
                    
                    
            if loytyiko == False: # ei löytynyt sanakirjasta
            
                uusi_valinta=input("Sanaa ei löytynyt. Haluatko lisätä sanan sanakirjaan (k/e)? ").lower().strip()
                if uusi_valinta=="k" :
                    uusi_selitys=input("Anna selitys hakusanalle\033[1m " + hakusana + "\033[0m: ").lower()
                    rivit['sanat'].append(({'sana': hakusana, 'selitys': uusi_selitys}))
                    # sortataan sanakirjan rivit hakusanan mukaan
                    rivit['sanat'] = sorted(rivit['sanat'], key=lambda k: k['sana'], reverse=False)
                            
                    with open('sanakirja.json', 'w') as tiedosto:
                        json.dump(rivit, tiedosto)
                        print("Uusi sana on lisätty onnistuneesti sanakirjaan.")

            tiedosto.close()
        else: print("Tuntematon valinta, yritä uudelleen!")

if __name__ == "__main__":
    main()




