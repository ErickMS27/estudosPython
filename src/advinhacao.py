print("*------------------------------*")
print("Bem vindo no jogo de Advinhação!")
print("*------------------------------*")

secret_number = 27
chances_number = 5
turn = 1

while(chances_number > 0):
        print("Tentativa:", turn, "de", chances_number)
        try_chance = input ("Digite o seu número: ")
        print("Você digitou:", try_chance)
        chance = int(try_chance)

        correct = chance == secret_number
        bigger = chance > secret_number
        smaller = chance < secret_number

        if (correct):
            print("Você acertou, parabéns!")
            play_again = input("Deseja jogar novamente? (s/n): ")
            if play_again.lower() != 's':
                break
        else:
            if(bigger):
                print("Você errou, é uma pena! Seu número foi maior do que o número secreto.")
            elif(smaller):
                print("Você errou, é uma pena! Seu número foi menor do que o número secreto.")

        turn = turn + 1

        if turn > chances_number:
            print("Limite de tentativas atingido. Fim de jogo")
            play_again = input("Deseja jogar novamente? (s/n): ")
            if play_again.lower() != 's':
                break
