'''
CONSTANTE = ¨Variáveis"que não vão mudar
muitas condições no mesmo if (ruim)
<- Contagem de complexidade (ruim)
'''

velocidade = 61  # velocidade atual d carro
local_carro = 100  # local em que o carro está na estrada

RADAR_1 = 60  # velocidade máxima do rar 1
LOCAL_1 = 100  # local onde o radas 1 está
RADAR_RANGE = 1  # A distancia onde o radar pega

velecidadeCarroPassouRadar1 = velocidade > RADAR_1
carroPassouRadar1 = local_carro >= (
    LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)

carroMultadoRadar1 = carroPassouRadar1 and velecidadeCarroPassouRadar1

if velocidade > RADAR_1:
    print('Velocidade carro passou do radar 1')

if carroMultadoRadar1:
    print('Carro multado')
