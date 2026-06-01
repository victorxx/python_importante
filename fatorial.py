numero=int(input("digite o fatorial"))
if numero >0 and type(numero) == int:
    fatorial =1
    for item in range(1,numero+1):
        fatorial=fatorial*item
        print(fatorial)
