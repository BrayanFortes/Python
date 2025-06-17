from datetime import datetime

DataNascimento = (input("""Digite Sua Data de Nascimento:
                        Exemplo: (dd/mm/aaaa) 
                    ->    """))
formatacao = datetime.strptime(DataNascimento, "%d/%m/%Y")
AnoAtual = datetime.now()

AnoNascimento = formatacao.strftime("%Y")
IdadeMinima = (AnoAtual.year - formatacao.year)
if IdadeMinima == 18:  
    print(f"""Sua data de Nascimento é {formatacao.strftime("%d/%m/%Y")}
Você ira fazer {IdadeMinima}, esse ano.
Já está na Hora certa de se Alistar, Jovem""")
elif IdadeMinima <= 17:
    Falta = IdadeMinima - 18
    Falta = (Falta*-1)
    print(f"""Sua data de Nascimento é {formatacao.strftime("%d/%m/%Y")}
Você ira fazer {IdadeMinima}, esse ano.
Ainda não está na Hora de se Alistar, Jovem
Falta {Falta} ano""")

elif IdadeMinima >= 19:
    Falta = IdadeMinima - 18
    print(f"""Sua data de Nascimento é {formatacao.strftime("%d/%m/%Y")}
***************************************************************          
Você ira fazer {IdadeMinima} anos de idade, esse ano.
Passou da Hora de se Alistar
Você atrasou {Falta} anos, do seu Alistamento""")
else:
    (print("Algo de Errado, Tente Novamente"))
print("""***************************************************************
Lembre-se, Todos devem se alistar durante o periodo, 1 de Junho a 30 de Junho 
***************************************************************""")