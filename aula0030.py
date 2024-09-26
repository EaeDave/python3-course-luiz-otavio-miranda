"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""

velocidade = 61  # velocidade atual do carro
local_carro = 90  # local em que o carro está na estrada

RADAR_1 = 60  # velocidade máxima do radar1
LOCAL_1 = 91  # local onde o radar 1 está
RADAR_RANGE = 1  # a distância onde o radar pega

passou_velocidade_radar1 = velocidade > RADAR_1
local_carro_range_radar1 = local_carro >= LOCAL_1 - RADAR_RANGE and \
    local_carro <= LOCAL_1 + RADAR_RANGE


if passou_velocidade_radar1 and local_carro_range_radar1:

    print('Passou da velocidade.')
else:
    print('Não passou da velocidade.')