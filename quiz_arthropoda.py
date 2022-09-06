'''
---------------------------------
| Quiz de Arthropoda            |
| Data: 06.09.2022              |
---------------------------------
'''

print ("Seja bem-vindo(a) ao meu quiz de Arthropoda!")

playing = input("Você quer jogar? ")

if playing.lower() != "sim":
    quit()

print("OK! Vamos jogar :)")
print("Instruções: Por favor, responda apenas com 'V' ou 'F'.")
score = 0

answer = input("Scolopendromorpha e Scutigeromorpha são ordens de Chilopoda R=")
if answer.upper() == "V":
    print('Acertou! :)')
    score += 1
else: 
    print("Errado :(")

answer = input("Os animais da ordem Orthoptera possuem os 2 pares de asas tégmina R=")
if answer.upper() == "F":
    print('Acertou! :)')
    score += 1
else: 
    print("Errado :(")

answer = input("O aparelho bucal dos animais da ordem Coleoptera é picador sugador R=")
if answer.upper() == "F":
    print('Acertou! :)')
    score += 1
else: 
    print("Errado :(")

answer = input("Os animais da ordem Opiliones NÃO apresentam pedicelo R=")
if answer.upper() == "V":
    print('Acertou! :)')
    score += 1
else: 
    print("Errado :(")

print("Sua pontuação foi " + str(score) + "/4")
print("Sua porcentagem de acerto foi " + str((score/4) * 100) + "%")