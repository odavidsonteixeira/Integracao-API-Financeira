import json
import requests
from datetime import date as dt
from tabulate import tabulate as tb


def getAPIInfo():
    global data
    url = 'https://api.hgbrasil.com/finance?format=json-cors&key=0d004f1b'
    request = requests.get(url)

    if request.status_code == 200:
        data = request.json()
    else:
        print('Falha na requisição!')

    return data


def getDol(data, dol):
    currency = data["results"]["currencies"]["USD"]
    nome = currency["name"]
    compra = currency["buy"]
    venda = currency["sell"]
    variacao = currency["variation"]

    dol.append(compra)


def getEuro(data, euro):
    currency = data["results"]["currencies"]["EUR"]
    nome = currency["name"]
    compra = currency["buy"]
    venda = currency["sell"]
    variacao = currency["variation"]

    euro.append(compra)


def getDate(date):
    now = dt.today().strftime("%d/%m/%Y")

    date.append(now)


def run():
    dol = []
    euro = []
    data = []

    getDate(data)
    dados = getAPIInfo()
    getDol(dados, dol)
    getEuro(dados, euro)

    rt = ['', 'Dólar', 'Euro']
    ls = [[rt[0], rt[1], rt[2]]]

    for x in range(len(data)):
        ls.append([data[x], dol[x], euro[x]])
    moedas = tb(ls, headers="firsttrow", tablefmt="grid")

    print(moedas)


run()
