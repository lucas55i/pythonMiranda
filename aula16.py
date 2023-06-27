# if  / elif       / else
# se / se não se / se não

entrada = input('Voce quer "entrar" ou "sair"\n')

if entrada == 'entrar':
    print('Voce ENTROU!')
elif entrada == 'sair':
    print('Voce saiu')
elif entrada == 'parei':
    print('Pareo')
else:
    print('Digite algo valido!')
print('Fora')