nomeCidade = input('Digite o nome da sua cidade: ').strip().upper()
print('A cidade {} começa com a palavra Santo? {}'.format(nomeCidade, 'SANTO' in nomeCidade[:5]))