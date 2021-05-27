from time import sleep
def ajudaplease(comando): 
    título(f'Acessando o manual de {comando}')
    help(comando)
    sleep(2)
def título(texto):
    tamanho = len(texto) + 4
    print('-' * tamanho)
    print(f'  {texto}')
    print('-' * tamanho)
    sleep(1)
ajuda = ''
while True:
    título('Sistema de ajuda Phyton')
    ajuda = str(input('Função ou biblioteca > '))
    if ajuda.upper() == 'FIM':
        título('Até logo')
        break
    else:
        ajudaplease(ajuda)
