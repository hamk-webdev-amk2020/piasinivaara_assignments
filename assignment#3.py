# -*- coding: cp1252 -*-
import urllib.request
def main():
    url = input("Anna url: ")
    polku=input("Anna polku: ")
    #testaan ensin että tiedosto on luettavissa
    try:
        response = urllib.request.urlopen(url)
    except Exception as ex:
        print("Virheellinen url", ex)
        return 0
    html = response.read()

    firstpos=url.rfind("/")
    lastpos=len(url)
    tiedosno_nimi = url[firstpos+1:lastpos]

    uusi_url = str(polku)+"/"+tiedosno_nimi
    #print(uusi_url)
    try:
        urllib.request.urlretrieve(url, uusi_url)
    except Exception:
        print("Tallennus uuteen paikkaan ei onnistunut", ex)
    else:
        print("Tallennus onnistui")

if __name__ == "__main__":
    main()





