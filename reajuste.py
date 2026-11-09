salario = float(input("Digite o salário atual: "))
tempo = int(input("Digite o tempo de serviço (em anos): "))

# Reajuste conforme a faixa salarial
if salario <= 500:
    reajuste = 25
elif salario <= 1000:
    reajuste = 20
elif salario <= 1500:
    reajuste = 15
elif salario <= 2000:
    reajuste = 10
else:
    reajuste = 0

novo_salario = salario + (salario * reajuste / 100)

if tempo < 1:
    bonus = 0
elif tempo <= 3:
    bonus = 100
elif tempo <= 6:
    bonus = 200
elif tempo <= 10:
    bonus = 300
else:
    bonus = 500

salario_final = novo_salario + bonus

print("===== RESULTADO =====")
print("Salário atual:", salario)
print("Reajuste:", reajuste, "%")
print("Salário reajustado:", novo_salario)
print("Bônus:", bonus)
print("Salário final:", salario_final)