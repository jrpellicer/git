#!/bin/python
# coding=utf-8

from bs4 import BeautifulSoup
import requests
import pandas as pd

URL = "https://resultados.as.com/resultados/futbol/primera/clasificacion/"
pagina = requests.get(URL)

if pagina != None and pagina.ok:
#    print(f"Pagina: {pagina}")
    soup = BeautifulSoup(pagina.content,"html.parser")
    eq = soup.find_all('span',class_="nombre-equipo")
    equipos = []
    cont = 0
    for i in eq:
        if cont < 20:
            equipos.append(i.text)
        else:
            break
        cont+=1
    cont = 0
    pt = soup.find_all('td',class_="destacado")
    puntos = list()
    for i in pt:
        if cont < 20:
            puntos.append(i.text)
        else:
            break
        cont+=1
    df = pd.DataFrame({'Nombre':equipos,"Puntos":puntos},index=list(range(1,21)))

    print(df)
    print("Hecho")

