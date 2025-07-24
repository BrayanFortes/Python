import requests
print("""/###########################################################################################################\\
                                                Conversão de Moeda
        Este programa converte uma quantia de dinheiro de uma moeda para outra usando a API ExchangeRates
/####################################################################################################################\\""".upper())

API_KEY = "aa7c59dda39ed745c1300fc174d89f25"
moeda1 = str(input("qual moeda você vc vai converter? Ex:(BRL)"))
quantia = float(input("Quanto de Dinheiro você tem? "))
print("|###################|\n 1- Dólar\n 2- Euro\n 3- Ienes\n 4- PesoMexicano \n 5- Escreva para qual será convertida? \n|###################| ")
opcao = int(input("Qual a Opção:"))

if opcao == 1:
    moeda2 = 'USD'
elif opcao == 2:
    moeda2 = 'EUR'
elif opcao == 3:
    moeda2 = 'JPY'
elif opcao == 4:
    moeda2 = 'BRL'
elif opcao == 5:
    moeda2 = str(input("Qual a Moeda que você quer converter? Ex:(USD)"))
    url = f"https://api.exchangeratesapi.io/v1/convert?access_key={API_KEY}&from={moeda1}&to={moeda2}&amount={quantia}"
else:
    print("Opção inválida!")
    exit()

url = f"https://api.exchangeratesapi.io/v1/convert?access_key={API_KEY}&from={moeda1}&to={moeda2}&amount={quantia}"

resposta = requests.get(url)
dados = resposta.json()

if 'result' in dados:
    conversao = dados['result']
    print(f"💱 {quantia:.2f} {moeda1} = {conversao:.2f} {moeda2}")
else:
    print("Erro na API:", dados)
