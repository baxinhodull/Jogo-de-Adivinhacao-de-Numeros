import random

def jogar():
    numero_minimo = int(input("Qual o número mínimo do intervalo?\n"))
    numero_maximo = int(input("Qual o número máximo do intervalo?\n"))
    
    
    while numero_minimo >= numero_maximo:
        print("O número mínimo deve ser menor que o número máximo.")
        numero_minimo = int(input("Qual o número mínimo do intervalo?\n"))
        numero_maximo = int(input("Qual o número máximo do intervalo?\n"))
    
    tentativas = int(input("Quantas tentativas para acertar?\n"))
    
    numero_sorteado = random.randint(numero_minimo, numero_maximo)

    while tentativas > 0:
        try:
            tentativa = int(input(f'Digite um número entre {numero_minimo} e {numero_maximo}.\n'))
            
            if tentativa == numero_sorteado:
                print("PARABÉNS VOCÊ ACERTOU O NÚMERO!")
                break
            else:
                tentativas -= 1
                if tentativa < numero_sorteado:
                    print("Tente um número maior!")
                elif tentativa > numero_sorteado:
                    print("Tente um número menor!")
                print(f'Você ainda tem {tentativas} tentativas.')
            
            if tentativas == 0:
                print(f'Você perdeu! O número sorteado era {numero_sorteado}.')
        
        except ValueError:
            print("Por favor, insira um número válido.")
    
    
    jogar_novamente = input("Você quer jogar novamente? (s/n)\n").lower()
    if jogar_novamente == 's':
        jogar()
    else:
        print("Obrigado por jogar!")


jogar()