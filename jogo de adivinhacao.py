print("*******************")
print("bem vindo ao jogo de adivinhação")
print("*******************")

numero_secreto = 5623

chute_str = input("digite o seu numero:")
print(" você digitou ", chute_str)
chute = int(chute_str)

if (numero_secreto == chute):
    print("Você acertou!")
    else:
        print("Você errou!")
        print("fim de jogo!")