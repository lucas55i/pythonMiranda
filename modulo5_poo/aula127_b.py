import json
from exercicios.aula127 import CAMINHO_ARQUIVO, Pessoa


with open(CAMINHO_ARQUIVO, 'r') as arquivo:
    pessoas = json.load(arquivo)

    for pessoa in pessoas:
        