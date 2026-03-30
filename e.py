#Algoritmo para calcular IMC
print("Bem-vindo ao calculador de IMC!")
nome = input("Digite seu nome: ")
print("Olá, {}!".format(nome) + " Este programa irá calcular o seu Índice de Massa Corporal (IMC).")
peso = float(input("{}, digite seu peso em kg: ".format(nome)))
altura = float(input("{}, digite sua altura em metros: ".format(nome)))
imc = peso / (altura ** 2)
print("{}, seu IMC é: {:.2f}".format(nome, imc))

