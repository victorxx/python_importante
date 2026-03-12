from bs4 import BeautifulSoup

html = """
<!DOCTYPE html>
<html lang="pt-br">
<body>

<table>
<tr>
<th>Produto</th>
<th>Preço</th>
</tr>

<tr>
<td>Arroz</td>
<td>R$ 20,00</td>
</tr>

<tr>
<td>Feijão</td>
<td>R$ 8,00</td>
</tr>

</table>

</body>
</html>
"""

soup = BeautifulSoup(html,'html.parser')
tds = soup.find_all('td')

for link in tds:
    if 'Arroz' in link.text:
        preco_tag = link.find_next('td')
        preco_texto = preco_tag.text
        
        print('Preço original:', preco_texto)

        preco_num = float(preco_texto.replace('R$', '').replace(',', '.'))

        if preco_num < 30:
            preco_tag.string = "R$30,00"

            mudar = preco_tag.text
            print("Preço novo:", mudar)
