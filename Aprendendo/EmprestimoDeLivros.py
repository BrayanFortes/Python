Livros = []
Usuarios = []
Emprestimo = []





def cadLivro():
    Id = len(Livros) + 1
    Nome = input("Nome do Livro:")
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
    



cadLivro()
ListLivros()