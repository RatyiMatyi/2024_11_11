"""Készíts egy programot, amely a felhasználótól kis "a" betűvel kezdődő szavakat kér be
és ezeket tárolja. Ha a felhasználó nem "a" betűvel kezdődő szót ad meg, akkor azt hagyja
figyelmen kívül és ne tárolja. A bekérés egészen addig folytatódjon, amíg a felhasználó
ENTER-t nem üt (nem ad meg újabb nevet a bekérésnél)! A program a bekért neveket írja ki
a képernyőre!

A program tájékoztatássa a felhasználót a működéséről, és az elvárt adatokról"""


szavak = []

while True:
    szo = input("Adj meg egy kis 'a' val kezdődő szót:").strip( )

    if szo == "":
        break

    if szo[0] == "a" or szo[0] == "A":
        szavak.append(szo)


print("A begyűjtött szavak", szavak)
