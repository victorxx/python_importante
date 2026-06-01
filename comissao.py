def calcular(valor,porcentagem):
    comissao=valor*porcentagem/100
    return comissao

venda=float(input('valor da venda'))
porcentagem=float(input('valor da porcentagem'))
resultado=calcular(venda,porcentagem)
print(resultado)
