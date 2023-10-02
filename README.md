# Bomb-Party-Portuguese 🇧🇷
*O jogo não possuí interface gráfica*
# ⭐ Como funciona o jogo?

## Digitando a palavra
Uma sílaba aparece na tela, e o jogador deverá escrever uma palavra da lingua portuguesa que contenha aquela sílaba, ou seja:
- A palavra digitada pode iniciar com a sílaba;
- A palavra pode terminar com a sílaba;
- A palavra pode conter a sílaba em outra posição.
  
## Vidas ❤️
### Perdendo vidas
O jogador inícia com um número específico de vidas, que podem ser pedidas caso:
- O jogador demore mais do que o tempo especificado para digitar a palavra.

Se a palavra digitada pelo jogador não for válida, ele não perde uma vida de ultimato, mas o seu tempo para digitar a próxima palavra é reduzido em 20%.
* Caso o jogador digite uma palavra já usada por ele anteriormente, a palavra será inválida também.

 ### Ganhando vidas
 Na tela, aparece uma lista de **letras** que o jogador deve usar em suas palavras, caso ele use todas, ele receberá uma vida extra, até o limite de vidas definido.

 # ⭐ Como jogar o jogo?
*é necessário o uso da versão 3 ou superior do **python** para que seja possível utilizar o programa*
  
## Importando o módulo "Imputiomeout" do python
Para que o programa funcione corretamente, é necessário realizar a instalação da biblioteca "Inputimeout".
### O que é?
* é uma biblioteca que permite uma funcionalidade para que haja um tempo limite para realizar um input, função essa usada no programa.

### instalando
abra o CMD do windows e digite o seguinte comando
```
pip install inputimeout
```
Desse modo, será instalada a biblioteca inputimeout em seu computador.

## Implementando 🎮

*Para evitar problemas, é recomendável baixar (ou pegar o código) dos arquivos **"bombPartyPT.py"** e **"palavras.txt"** e deixá-los no **mesmo diretório**.*
Após isso, crie um programa (ou baixe/pegue o código do arquivo "main.py") para ser o seu programa principal, ou seja, onde você importará o módulo do arquivo **"bombPartyPT"**

Feito isso, basta importar o módulo "bombPartyPT" e usar a função **"play"** passando **3 parâmetros** principais:
- vidas_inicias:int -> será o número de vidas que o jogador irá começar o jogo;
- vidas_finasi:int -> será o número de vidas máxima que o jogador poderá obter jogando;
- tempo:float -> será o tempo que o jogador terá para digitar a palavra (em segundos).

exemplo:
  
```
import bombPartyPT

bombPartyPT.jogar(1, 5, 7)
```
Com isso, basta rodar o programa e o jogo estará funcionando.

# Vídeo do jogo em execução 📹

https://github.com/drcrls/Bomb-Party-Portuguese/assets/129799424/b3096ae6-095e-49dd-be0d-8691ba257919


