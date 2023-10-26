import requests
import sys
from bs4 import BeautifulSoup

# Analiza los plugins de las paginas web.

def main():
    url = ""
    agent = {"User-Agent": "Firefox"}
    peticion = requests.get(url=url, headers=agent)
    soup = BeautifulSoup(peticion.text, 'html.parser')

    lista_plugin = []
    lista_final = []

    for enlace in soup.find_all('link'):
        if '/wp-content/plugins' in enlace.get('href'):
            href = enlace.get('href')
            href = href.split("/")
            posicion = href.index("plugins")
            plugin = href[posicion + 1]
            lista_plugin.append(plugin)

    # Si se encuentra un plugin nuevo lo añade a la lista final,si no pasa,ya que esto se hace para que los plugins no salgan repetidos
    for i in lista_plugin:
        if i in lista_final:
            pass
        else:
            lista_final.append(i)

    for i in lista_final:
        print(f"(+) Se encontro el plugin {i}")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
