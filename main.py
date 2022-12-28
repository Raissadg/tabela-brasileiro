import requests
from bs4 import BeautifulSoup
from tabulate import tabulate


headers = {'User-agent': 'Mozilla/5.0'}
resposta = requests.get('https://www.cnnbrasil.com.br/esporte/futebol/tabela-brasileirao-serie-a-2022/', headers = headers)

soup = BeautifulSoup(resposta.text, 'html.parser')
linhas = soup.find("div", {"class":"table__info"}).find("tbody").find_all("tr")

brasileirao = []
cabecalho = ["CLASSIFICAÇÃO", "TIME", "PARTIDA", "JOGOS", "VITÓRIAS", "EMPATE", "DERROTAS", "GOLS", "GOLS CONTRA", "SALDO DE GOLS"]

for linha in linhas:
	dados = linha.find_all("td")
	times = dados[0].text.split()
	posicao = times[0]
	time = times[1]
	partidas = dados[1].text
	jogos = dados[2].text
	vitorias = dados[3].text
	empates = dados[4].text
	derrotas = dados[5].text
	gols = dados[6].text
	gols_contra = dados[7].text
	saldo_gols = dados[8].text
	brasileirao.append([posicao, time, partidas, jogos, vitorias, empates, derrotas, gols, gols_contra, saldo_gols])


print(tabulate(brasileirao, cabecalho, tablefmt="fancy_grid"))
