n1 = float(input("Digite o valor da primeira nota: "))
n2 = float(input("Digite o valor da segunda nota: "))
n3 = float(input("Digite o valor da terceira nota: "))

n4 = n1+n2+n3
me = n4/3


ma = (n1 + n2*2 + n3*3 + me)/7  


if ma >= 9:
    conceito = "A"
elif ma >= 7.5:
    conceito = "B"
elif ma >= 6:
    conceito = "C"
elif ma >= 4:
    conceito = "D"
else:
    conceito = "E"

print("Média de aproveitamento: {:.2f}".format(ma))
print("Conceito:", conceito)