import random

def escolher_palavra():
    palavras = ['python', 'programacao', 'desenvolvimento', 'computador', 'jogo']
    return random.choice(palavras)

def exibir_forca(tentativas):
    estagios = [
        '''
           -----
           |   |
           |   O
           |  /|\\
           |  / \\
           |
        ''',
        '''
           -----
           |   |
           |   O
           |  /|\\
           |  /
           |
        ''',
        '''
           -----
           |   |
           |   O
           |  /|
           |
           |
        ''',
        '''
           -----
           |   |
           |   O
           |
           |
           |
        ''',
        '''
           -----
           |   |
           |
           |
           |
           |
        ''',
        '''
           -----
           |
           |
           |
           |
           |
        ''',
    ]
    return estagios[tentativas]

def jogar():
    palavra_secreta = escolher_palavra()
    letras_adivinhadas = []
    tentativas = 5
    vitoria = False

    print("Bem-vindo ao Jogo da Forca!")

    while not vitoria and tentativas > 0:
        print(exibir_forca(tentativas))
        print("Palavra:", end=' ')

        for letra in palavra_secreta:
            if letra in letras_adivinhadas:
                print(letra, end=' ')
            else:
                print('_', end=' ')

        print("\n\nLetras já adivinhadas: ", ' '.join(letras_adivinhadas))

        tentativa = input("Advinhe uma letra: ").lower()

        if tentativa in letras_adivinhadas:
            print("Você já tentou essa letra. Tente outra.")
        elif tentativa in  palavra_secreta:
            letras_adivinhadas.append(tentativa)
            print("Boa! A letra está na palavra.")
        else:
            letras_adivinhadas.append(tentativa)
            tentativas -= 1
            print("Ops! A letra não está na palavra.")
        
        if all(letra in letras_adivinhadas for letra in palavra_secreta):
            vitoria = True

    if vitoria:
        print(f"Parábens! Você adivinhou a palavra:  {palavra_secreta}")
    else:
        print(exibir_forca(tentativas))
        print(f"Você perdeu! A palavra era: {palavra_secreta}")

if __name__ == "__main__":
    jogar()