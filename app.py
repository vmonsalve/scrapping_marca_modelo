from Helpers.scrapping import extrae_marcas
from Helpers.marcasDba import obtener_marcas, obtener_marca
from Models.marca import Marca
from Models.modelo import Modelo
from lxml import html
import requests
import os
from dotenv import load_dotenv

load_dotenv()

url_base = os.getenv('URL_BASE')
marca = obtener_marca(int(1))

url_marca = url_base+marca.url
page_marca = requests.get(url_marca)
tree = html.fromstring(page_marca.content)

contenedor_modelos = tree.xpath('/html/body/main/section[1]/div/div')
divs = len(contenedor_modelos[0].xpath('./div'))
for i in range(1, divs+1):
    modelo = tree.xpath('/html/body/main/section[1]/div/div/div['+str(i)+']/a/div/span[2]')[0].text
    print(f"marca {marca.nombre} modelo {modelo}")