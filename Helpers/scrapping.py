from .marcasDba import insertar_marca
from lxml import html
import requests
import os

def extrae_marcas():
    url_base = os.getenv('URL_BASE')
    page = requests.get(url_base+'/catalogo')
    tree = html.fromstring(page.content)

    contenedor = tree.xpath('/html/body/main/section[1]/div/div')
    divs = len(contenedor[0].xpath('./div'))
    
    for i in range(1, divs+1):
        marca = tree.xpath('/html/body/main/section[1]/div/div/div['+str(i)+']/a/p[1]')[0].text
        href = tree.xpath('/html/body/main/section[1]/div/div/div['+str(i)+']/a/@href')[0]
        insertar_marca(marca, href)