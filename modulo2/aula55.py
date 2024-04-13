"""
Higher Order Functions
Funções de primeira classe
"""

def saudacao(msg):
    return msg

def executa(funcao, msg):
    return funcao(msg)

saudacao_2 =  saudacao
v = executa(saudacao, 'Bom dia')
print(v)