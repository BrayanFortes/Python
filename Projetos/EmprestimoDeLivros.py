Livros = []
Usuarios = []
Emprestimo = []





def cadLivro():
    Id = len(Livros) + 1
    Nome = input("Nome do Livro:").lower()
    Autor = input("Nome do Autor:")
    Livros.append ({"id": Id,"NomeLivro": Nome, "Autor": Autor, "Disponível": True })
    print("Cadastrado com Sucesso")

def ListLivros():
    for Livro in Livros:
        Status = "Disponivel" if Livro['Disponível'] == True  else "Não Disponivel"
        print(f"Id: {Livro['id']}\nLivro: {Livro['NomeLivro']}\nStatus: {Status}")

def Usuario():
    User = input("Seu Nome:")
    Cpf = input ("CPF:")
    Usuarios.append({"Nome": User, "CPF": Cpf})
    print("Usuário Cadastrado com Sucesso")

def EmprestimoLivro():
    escolha = input("Digite o Nome do Livro que deseja emprestar:").lower()
    livrocerto = None

    for Livro in Livros:
        if Livro['NomeLivro'] == escolha and Livro['Disponível']:
            livrocerto = Livro
            break

    if livrocerto:
        print("Livro Disponível para Emprestimo")
        opcao = input("Tem certeza que deseja emprestar este livro? (S/N):").upper()
        if opcao == 'S': 
            Emprestimo.append({"Usuario": Usuarios[-1], "Livro": livrocerto})
            print("Emprestimo realizado com sucesso!")
            print("O Livro foi emprestado para:", Usuarios[-1]['Nome'])
            print(f"Pertencente do CPF {Usuarios[-1]['CPF']}")
        else:
            print("Emprestimo cancelado.")
    else:
        print("Livro não encontrado ou não disponível para emprestimo.")




cadLivro()
ListLivros()
Usuario()
EmprestimoLivro()

#ListLivros()
#Usuario()
#EmprestimoLivro()#