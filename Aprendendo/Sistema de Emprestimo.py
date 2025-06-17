valorCasa = int(input("Valor da Casa: R$"))
Salario = int(input("Salário do Comprador: R$"))
tempo = float(input("Quanto tempo para pagar ? "))
def parcela():
    global tempo
    tempo = tempo * 12 
parcela()    
valorMensal = valorCasa / tempo
if valorMensal > Salario * 0.30:
    print("Emprestimo NEGADO")
else:
    print("Emprestimo APROVADO")
    print(f'Valor a ser PAGO durante {tempo:.0f} meses:\nR${valorMensal:.2f}')