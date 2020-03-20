
def escrever_arquivo(texto):
    arquivo = open('teste.txt', 'w')
    arquivo.write('Minha primeira escrita \n')
    arquivo.close()

def atualizar_arquivo(texto):
    arquivo = open('teste.txt', 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    print(aluno_nota)
    aluno_nota = aluno_nota.split('\n')
    print(aluno_nota)
    for x in aluno_nota:
        print(x)

if __name__ == '__main__':
    # escrever_arquivo('Primeira linha. \n')
    # aluno = 'Giovana, 10, 10, 5, 5'
    # atualizar_arquivo('notas.txt, aluno')
    # ler_arquivo('teste.txt')