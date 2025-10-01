def avaliar(velocidade):
    if velocidade >60:
        print("recebe multa")
    else:
        print("esta liberado")

print("qual foi sua velocidade na pista?: ")
velocidade = int(input())

avaliar(velocidade)