Este é um jogo simples de adivinhação de números em Python. O objetivo do jogo é adivinhar o número sorteado dentro de um intervalo fornecido pelo usuário, dentro de um número limitado de tentativas.

Funcionalidades
O jogo permite ao usuário definir o intervalo de números (mínimo e máximo) em que o número será sorteado.
O usuário tem um número específico de tentativas para adivinhar o número sorteado.
Após cada tentativa, o jogo dá dicas: "Tente um número maior!" ou "Tente um número menor!".
O jogo termina quando o usuário acerta o número ou esgota as tentativas.
O usuário pode optar por jogar novamente após o fim de uma partida.
Como Rodar o Código
Pré-requisitos: Este código requer Python 3.x instalado no seu computador.

Executando o Jogo:

Abra um terminal ou prompt de comando.
Navegue até o diretório onde o arquivo Python (jogo.py) está localizado.
Execute o comando:
python jogo.py
Regras:

O programa vai solicitar que você informe o número mínimo e máximo do intervalo.
Em seguida, ele pedirá para você indicar quantas tentativas terá para adivinhar o número sorteado.
A cada tentativa, o programa vai dar uma dica se o número inserido for maior ou menor que o número sorteado.
Você pode escolher jogar novamente após o fim de cada rodada.
Exemplo de Execução
Qual o número mínimo do intervalo?
1
Qual o número máximo do intervalo?
100
Quantas tentativas para acertar?
5
Digite um número entre 1 e 100.
50
Tente um número menor!
Você ainda tem 4 tentativas.
Digite um número entre 1 e 100.
30
Tente um número maior!
Você ainda tem 3 tentativas.
Digite um número entre 1 e 100.
40
PARABÉNS VOCÊ ACERTOU O NÚMERO!
Você quer jogar novamente? (s/n)
n
Obrigado por jogar!
Detalhes do Código
Entrada de Dados:

O usuário escolhe o intervalo de números (mínimo e máximo).
O número de tentativas também é definido pelo usuário.
Lógica:

O número sorteado é escolhido aleatoriamente entre o intervalo fornecido.
O usuário tem um número limitado de tentativas para adivinhar o número sorteado.
Se o número informado for menor ou maior que o sorteado, o jogo fornece dicas para ajustar a próxima tentativa.
Repetição:

O jogo pergunta se o usuário quer jogar novamente ao final de cada rodada.
O jogo continua até o usuário decidir não jogar mais.
Tecnologias Usadas
Python 3.x
Biblioteca random (para gerar números aleatórios)
Licença
Este projeto é de código aberto. Sinta-se livre para usar, modificar e distribuir conforme desejar.

