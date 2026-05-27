import customtkinter as ctk

ctk.set_apperance_mode("Dark")
ctk.set_default_color_theme("pink")

janela = ctk.CTk()
                         
print("JOGO DE RPG")

nome_do_jogador = (input("Escolha um nome de usuário: "))

print(f"Ótimo {nome_do_jogador}, vamos começar o jogo.")


print("1 - Humano")
print("2 - Elfo")
print("3 - Mago")
print("4 - Fada")
print("5 - Cavalheiro")
classe = (input("Escolha a sua classe: "))

if classe == 1 :
    vida = 75
    força = 45
    equipamento = "Faca"
    experiência =  10

elif classe == 2 :
    vida = 60
    força = 30
    equipamento = "Graveto"
    experiência =  40

elif classe == 3 :
    vida = 70
    força = 20
    equipamento = "Varinha"
    experiência =  80

elif classe == 4 :
    vida = 20
    força = 20
    equipamento = "Sal da felicidade"
    experiência =  8

else : 
    vida = 80
    força = 90
    equipamento = "Espada"
    experiência =  30
    
