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
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in abrir:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        abrir.close
    
def cadastrar(arquivo,nome ='desconhecido',idade=0):
    try:
        abrir = open(arquivo,'at')
    except:
        print('Erro ao abrir o arquivo!')
    else:
        try:
            abrir.write(f'{nome};{idade}\n')
        except:
            print('Erro ao adicionar os dados fornecidos')
        else:
            print(f'Registro de {nome} adicionado com sucesso!')
            abrir.close
