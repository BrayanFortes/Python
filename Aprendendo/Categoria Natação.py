from datetime import datetime


AnoAtual = datetime.now()
nome = str(input("Digite seu nome:"))
Nasc = (input("""Sua data de Nascimento:
Ex:dd/mm/aaaa
->"""))

idade = datetime.strptime(Nasc, '%d/%m/%Y')
converta = AnoAtual.year - idade.year
Categorias = ['Mirin I', 'Mirin II', 'Petiz I', 'Petiz II', 'Infantil I', 'Infantil II', 'Juvenil I', 'Juvenil II', 'Júnior I', 'Júnior II', 'Sênior']
faixa = [9,10,11,12,13,14,15,16,17,18,19]
for i in range(len(faixa)):
    if converta == faixa[i] or (i == len(faixa) - 1 and converta >= faixa[i]):
       sub = Categorias[i]
print(f"""Nome: {nome}
Idade: {converta}
Categoria: {sub}""")
# Este código determina a categoria de natação de uma pessoa com base na sua idade.