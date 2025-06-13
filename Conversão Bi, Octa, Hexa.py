Decimal = int(input('Diga um número Decimal:'))
print("/*******************\n  1 - BINARIO\n  2 - OCTAL\n  3 - HEXADECIMAL\n /*******************\ ")
opcao =  int(input("Opção: "))
if opcao == 1:
    def converter():
        global Decimal
        Decimal = bin(Decimal)

elif opcao == 2:
    def converter():
        global Decimal
        Decimal = oct(Decimal)
elif opcao == 3:
    def converter():
        global Decimal
        Decimal = hex(Decimal)
converter()
print(Decimal[2:].upper())