# calculo de imc

print("calculadora de imc")
nome = input("digite seu nome: ")
peso = float(input("digite seu peso: "))
altura = float(input("digite sua altura: "))
imc = peso / (altura * altura)
print(nome, "seu imc =", imc)
