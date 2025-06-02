import requests

API_KEY = "aa7c59dda39ed745c1300fc174d89f25"
moeda1 = 'BRL'
quantia = float(input("Quanto de Dinheiro você tem? R$"))
print("|###################|\n 1- Dólar\n 2- Euro\n 3- Ienes\n|###################| ")
opcao = int(input("Qual a Opção:"))

if opcao == 1:
    moeda2 = 'USD'
elif opcao == 2:
    moeda2 = 'EUR'
elif opcao == 3:
    moeda2 = 'JPY'
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
