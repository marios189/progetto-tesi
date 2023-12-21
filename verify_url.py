import requests

def verify_url(url):
    try:
        response = requests.get(url)

        if response.status_code == 200:
            print("L'URL "+url+" ha una pagina web.")
        else:
            print("L'URL "+url+ " esiste, ma ha restituito un codice di stato " + {response.status_code})

    except requests.ConnectionError:
        print("Errore: Impossibile connettersi all'URL "+url)

url_da_verificare = 'https://www.diretta.it'
verify_url(url_da_verificare)