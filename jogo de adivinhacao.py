print("*******************")
print("bem vindo ao jogo de adivinhação")
print("*******************")
numero_secreto = 53
total_de_tentativas = 5
rodada = 1 

while (rodada <= total_de_tentativas):
    print("tentativa {} de {}".format(rodada, total_de_tentativas))

chute_str = input("digite o seu numero:")
print(" você digitou ", chute_str)
chute = int(chute_str)

acertou = chute == numero_secreto
maior = chute > numero_secreto
menor = chute < numero_secreto


    if (acertou):
    print("Você acertou!")
    else:
        if(maior):
        print("o seu chute e maior que o numero secreto")
        elif(menor):
            print("o seu chute é menor q o numero secreto")
rodada = rodada + 1






        print("fim de jogo!")