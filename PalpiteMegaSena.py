from time import sleep
lista = []
print('-'*32)
print('{:^32}'.format('JOGA NA MEGA SENA'))
print('-'*32)
n = int(input('Quantos jogos você quer jogar? '))
print(f'  -=-= SOETEANDO {n} JOGOS =-=-'), sleep(1)
print('Em ...', end=''), sleep(1.5), print(' 1', end=' - '), sleep(1.5), print('2', end=' - '), sleep(1.5), print('3')
print()
for mega in range(n):
    lista = [randint(0, 60), randint(0, 60), randint(0, 60), randint(0, 60),
             randint(0, 60), randint(0, 60)] 
    print(f'Jogo {mega + 1}: {sorted( lista )}')
    sleep(1)
print()
print('   -=-= < BOA SORTE! > =-=-')
print()
