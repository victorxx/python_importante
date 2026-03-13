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
<td>Xbox</td>
<td>2000</td>
</tr>

<tr>
<td>PlayStation</td>
<td>3000</td>
</tr>
</table>
</body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser')

tds = soup.find_all('td')  # lista de todas as células <td>
print("Número de <td> na tabela:", len(tds))

# Itera sobre cada <td>
for x in tds:
    if 'Xbox' in x.text:  # verifica se é o produto Xbox
        preco_tag = x.find_next('td')  # pega a tag do preço
        preco = int(preco_tag.text)    # converte para inteiro

        if preco > 100:
            print('Preço alto:', preco)
            # altera o preço diretamente na tabela
            preco_tag.string = "1500"  # novo preço
            print('Preço modificado:', preco_tag.text)  # mostra o novo valor

