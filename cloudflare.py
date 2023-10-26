import requests
import sys


def main():
    website = input("Ingresa la web")
    palabra = "cloudflare"
    url = requests.get(website)
    cabeceras = dict(url.headers)
    verificacion = False

    for cabecera in cabeceras:
        if palabra in cabeceras[cabecera].lower():
            verificacion = True
            break
    if verificacion == True:
        print("El sitio web tiene CloudFlare")
    else:
        print("El sitio web no tiene Cloudflare")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
