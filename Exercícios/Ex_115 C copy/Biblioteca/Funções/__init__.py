from Biblioteca.Menu import cabeçalho
def arquivoExiste(nome):
    try:
        abrir = open(nome,'rt')
        abrir.close()
    except(FileNotFoundError):
        return False
    else:
       return True

def criaarquivo(nome):
    try:
        criar = open(nome, 'wt+')
        criar.close()
    except:
        print('Houve um problema com a criação do arquivo!')
    else:
        print(f'Arquivo {nome} foi criado com sucesso!')

def lerarquivo(nome):
    try:
        abrir = open(nome, 'rt')
    except:
        print('Erro ao ler arquivo!')
    else:
        cabeçalho('Pessoas cadastradas')
        print(abrir.read())
