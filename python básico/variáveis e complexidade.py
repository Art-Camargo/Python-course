RADAR = 60
RANGE_RADAR = 1
QUILOMETRAGEM_DO_RADAR = 100

velocidade = 68.9
quilometro_carro = 99

if velocidade > RADAR and (quilometro_carro >= (RANGE_RADAR - QUILOMETRAGEM_DO_RADAR) and quilometro_carro <= (RANGE_RADAR + QUILOMETRAGEM_DO_RADAR)):
    print(f'Você foi multado, pois passou {velocidade - RADAR:.2f} de km acima do comportado na via pública!')
else:
    print('Você não foi multado')