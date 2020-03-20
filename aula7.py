
from aula8contador_letras import contador_letras

if __name__ == '__main__':
    lista = ['cachorro', 'gato', 'elefante']
    print(contador_letras(lista))
    total_letras = contador_letras(lista)
    print('Total de letras por palavras da lista {} ' .format(total_letras))






# from aula7TV import Televisao
# from aula7calculadora1 import Calculadora
#
# if __name__ == '__main__':
#     Televisao = Televisao()
#     print(Televisao.ligada)
#     Televisao.power()
#     print(Televisao.ligada)
#     calculadora = Calculadora(5, 10)
#     print(calculadora.soma())