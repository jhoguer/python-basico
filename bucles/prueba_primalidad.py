def primo(numero):
    contador = 0

    for i in range(2, numero):
        if numero % i == 0:
            contador += 1
            break    
    if contador == 0:
      return True
    else:
      return False



def run():
    numero = int(input('Escribe un numero: '))

    es_primo = primo(numero)
    if es_primo == True:
        print('El numero ' + str(numero) + " es primo")
    else:
        print('El numero ' + str(numero) + " NO es primo")


if __name__ == '__main__':
    run()
