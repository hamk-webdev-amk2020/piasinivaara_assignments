import json
from copy import deepcopy

try:
    tiedosto=open("sanakirja3.txt","r")
    tiedosto.close()
except Exception:
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

    with open('sanakirja3.txt', 'w') as tiedosto:
        json.dump(sorted_data, tiedosto)
    
    tiedosto.close()

while True:
    print ("\nSanakirja: ")
    print ("(1) Etsi sana sanakirjasta ")
    print ("(2) Näytä sanakirjan sisältö ")
    print ("(3) Poistu ohjelmasta")
    valinta = input("Valitse toiminto: ")
    valinta=valinta.strip()

    if valinta=="2":
        print("Sanakirjan sisältö on:\n")
        with open('sanakirja3.txt') as tiedosto:
            rivit = json.load(tiedosto)
            for i in rivit['sanat']:
                print('Sana:    ' + i['sana'])
                print('Selitys: ' + i['selitys'])
                print('')
        tiedosto.close()

    elif valinta=="3": 
        print("Poistuit sanakirjasta. Tervetuloa uudelleen!")
        break

    elif valinta=="1":
        hakusana=input("Anna hakusana: ").lower().strip()
        with open('sanakirja3.txt') as tiedosto:
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
                uusi_selitys=input("Anna selitys hakusanalle\033[1m " + hakusana + "\033[0m: ")
                rivit['sanat'].append(({'sana': hakusana, 'selitys': uusi_selitys}))
                # sortataan sanakirjan rivit hakusanan mukaan
                rivit['sanat'] = sorted(rivit['sanat'], key=lambda k: k['sana'], reverse=False)
                           
                with open('sanakirja3.txt', 'w') as tiedosto:
                    json.dump(rivit, tiedosto)
                    print("Uusi sana on lisätty onnistuneesti sanakirjaan.")

        tiedosto.close()
    else: print("Tuntematon valinta, yritä uudelleen!")




