altura = float(input("Digite sua altura: " ))
sex = int(input("Digite 1 para o sexo másculino e 2 para o feminino: "))

if sex == 1:
    peso = (72.7 * altura) - 58
    print("Seu peso ideal é ", peso)

elif sex == 2:
    peso = (62.1 * altura) - 44.7
    print("Seu peso ideal é ", peso)
else:
    print("Sexo inválido")