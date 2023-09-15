print('{:^9}'.format('  CADASTRO BASICO'))
p = t = h = m = d = 0
while True:
    print('='*19)
    print('Cadastre uma pessoa'.upper())
    print('-'*19)
    idade = int(input('Idade: '))
    if idade >= 18:
        t += 1
    elif idade < 18:
        p += 1 
    sexo = str(input('Sexo: [M/F] ')).strip().upper()
    if sexo == 'F':
        m += 1
    if sexo == 'F' and idade < 18:    
        d += 1
    if sexo == 'M':
        h += 1
    print('='*19)
    sair = str(input('''Quer continuar? [S/N] ''')).upper()
    if sair == 'N':
        break
    elif sair == 'S':
        continue
    elif sair != 's/n':
        print('Opção errada')
        break
print('{:-^30}'.format(' RESULTADO '))
print(f'Temos {t} pessoas maiores de 18 anos')
print(f'Total de {h} Homens e {m} Mulheres catrastradas. '"\n"'Com total de {} menores de 18 anos, sendo {} Mulheres'.format(p, d))
print('='*30)
