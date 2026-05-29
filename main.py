import random
import time

# Essas duas importações server uma para sortear números e tempo

#Para fazer o texto aparecer sendo digitado como uma máquina antiga

def digitar(texto, velocidade = 0.1): #está definindo tempo dentro do texto
    for letra in texto:
        print(letra, end='', flush=True)
        time.sleep(velocidade)
    print()

digitar('JOGO DE RPG')
time.sleep(1)

digitar("Escolha um nome de usuário: ")


nome_do_jogador = input

digitar(f"Ótimo {nome_do_jogador}, vamos começar o jogo.")

print("1 - Humano")
print("2 - Elfo")
print("3 - Mago")
print("4 - Fada")
print("5 - Cavalheiro")
digitar('Escolha a sua classe:')
time.sleep(1)
classe = (int(input))

if classe == 1 :
    vida = 75
    força = 45
    equipamento = "Faca"
    experiência =  10
    nomedaclasse = 'Humano'

elif classe == 2 :
    vida = 60
    força = 30
    equipamento = "Graveto"
    experiência =  40
    nomedaclasse = 'Elfo'

elif classe == 3 :
    vida = 70
    força = 20
    equipamento = "Varinha"
    experiência =  80
    nomedaclasse = 'Mago'

elif classe == 4 :
    vida = 20
    força = 20
    equipamento = "Sal da felicidade"
    experiência =  8
    nomedaclasse = 'Fada'

else : 
    vida = 80
    força = 90
    equipamento = "Espada"
    experiência =  30
    nomedaclasse = 'Cavalheiro'

print(f"Status da classe: {nomedaclasse}")
print(f'''           Vida: {vida}hp.
           Força: {força}.
           Equipamento: {equipamento}.
           Experiência: {experiência}xp.
      ''')
