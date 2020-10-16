# Ohjelma etsii ladatusta url:sta kiellettyjä sanoja

from urllib.request import urlopen
from bs4 import BeautifulSoup


def main():
    
    forbidden = ["Mobiilinäkymä", "Python", "Iman", "Ziggy",
                 "Berlin", "Blackstar", "Mars", "Hunky", "Spiders", "year"]
   

    url = "https://fi.wikipedia.org/wiki/Python_(savenvalaja)"
    html = urlopen(url).read()
    html_text = BeautifulSoup(html, features="html.parser")

    # remove all script and style elements
    for script in html_text(["script", "style"]):
        script.extract()    

    text = html_text.get_text()

    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)

    count=0
    for x in range(len(forbidden)): 
        count+=text.count(forbidden[x])
        
    print(count)
    #print(text)

if __name__ == "__main__":
    main()
