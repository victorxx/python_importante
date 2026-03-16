import requests
from bs4 import BeautifulSoup


url="http://localhost/teste/index.php"
response=requests.get(url)
soup=BeautifulSoup(response.text,'html.parser')
paragrafo=soup.find_all('p')
jesus=[p for p in paragrafo if 'jesus' in p.get_text()]
if jesus:
    print('ok tem sim')
else:
    print('não tem')
