from os import system, path
from random import randint
from inputimeout import inputimeout

caminho = path.dirname(__file__) + "\\palavras.txt"
with open(caminho, "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()
    palavras = ''.join(linhas[0]).split()
    incognitas = ''.join(linhas[1]).split()

def jogar(vidas_iniciais:int, vidas_finais:int, tempo:float):
    """Digite uma palavra da Língua Portuguesa usando a sílaba que está aparecendo. Após usar todas as letras, o jogador recebe uma vida extra."""
    if vidas_finais < vidas_iniciais:
        return
    
    vidas_atuais = vidas_iniciais
    letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v"]

    usadas = []
    def interface(sequencia):
        system('cls')
        print(f"\t{sequencia}\nLetras a serem usadas:")
        for i in letras:
            print(i, end=" ")
        print(f"\n{vidas_atuais} vida(s)")

    while vidas_atuais > 0:
        sequencia = incognitas[randint(0, len(incognitas)-1)]
        interface(sequencia)
        passou = False
        word = ''
        desconto_tempo = 0
        while passou == False:
            try:
                word = inputimeout("palavra:", tempo-desconto_tempo)
                if (sequencia not in word.casefold() or word.casefold() not in palavras) or word.casefold() in usadas:
                    print("erro")
                    desconto_tempo += tempo * 0.2

                else:
                    usadas.append(word)
                    if len(letras) > 0:
                        for i in word.casefold():
                            if i in letras:
                                letras.remove(i)
                                if len(letras) == 0:
                                    letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v"]
                                    vidas_atuais +=1
                    passou = True

            except Exception:
                print("tempo acabou")
                vidas_atuais -= 1
                break

    system('cls')
    print(f"fim de jogo\nacertos:{len(usadas)}")