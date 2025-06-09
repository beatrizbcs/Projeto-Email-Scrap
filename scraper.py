import requests
from bs4 import BeautifulSoup

url = "https://www.bbc.com/"
resposta = requests.get(url)
soup = BeautifulSoup(resposta.text, "html.parser")
dados = soup.find_all("p")

informacoes = "\n".join([d.text for d in dados])