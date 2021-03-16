times = 'Corinthians', 'Palmeiras', 'Santos', 'Flamengo', 'Fluminense',\
        'Avai', 'Chapecoense', 'Botafogo','Portuguesa', 'Bragantino'
print(f'Lista de times do Brasileirão: {times}')
print(f'Os 5 primeiros são: {times[:5]}')
print(f'Os 4 últimos são: {times[-4:]}')
print(f'Time em ordem alfabética: {sorted(times)}')
print(f'O Chapecoense está na {times.index("Chapecoense") +1}° posição')
