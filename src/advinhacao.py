print("*------------------------------*")
print("Bem vindo no jogo de Advinhação!")
print("*------------------------------*")

secret_number = 42

try_chance = input ("Digite o seu numero: ")

print("Você digitou:", try_chance)

chance = int(try_chance)

correct = chance == secret_number
bigger = chance > secret_number
smaller = chance < secret_number

if (correct):
    print("Você acertou, parabéns!")
else:
    if(bigger):
        print("Você errou, é uma pena! Seu número foi maior do que o número secreto.")
    elif(smaller):
        print("Você errou, é uma pena! Seu número foi menor do que o número secreto.")

print("Fim de Jogo")
