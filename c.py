#Algoritmo calcular o reajuste com imposto em um produto

preco = float(input("digite o preco: "))
reajuste = float(input("digite o reajuste: "))
imposto = float(input("digite o imposto: "))

preco_r = preco + (preco * reajuste / 100)
preco_f = preco_r + (preco_r * imposto / 100)

print("preco final =", preco_f)
