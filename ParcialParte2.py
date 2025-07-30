def mcd(a,b):
    if b == 0:
        return a
    else:
        return mcd(b,a%b)
def repetidor(palabra, numero):
    if numero == 1:
        return palabra
    else:
        nuevaPalabra = palabra + repetidor(palabra, numero-1)
        return nuevaPalabra
def letraVeces(palabra, letra, cont):
    if letra in palabra:
        cont += 1
        palabra.remove(letra)
        return letraVeces(palabra, letra, cont)
    else:
        return cont
def Binario(numero):
    return 0
def contarDigitos(numero, divisor, cont):
    n = numero/divisor
    print(n)
    if n > 0:
        cont = contarDigitos(numero, (divisor*10), cont+1)
        return cont
    else:
        return 0


while True:
    print("1. Calcular MCD de dos numeros.")
    print("2. Crear una cadena repetida N veces")
    print("3. Contar cuantas veces aparece una letra en una cadena")
    print("4. Convertir un numero decimal a binario")
    print("5.Calcular cuantos digitos tiene un numero")
    print("6. SALIR")
    opcion = int(input("Ingrese una opcion: "))
    match opcion:
        case 1:
            a = int(input("Ingrese el primer número:"))
            b = int(input("Ingrese el segundo número"))
            resultado = mcd(a,b)
            print(f"El MCD de los numeros: {a}, {b} es: {resultado}")
        case 2:
            palabra = input("Ingrese la palabra: ")
            numero = int(input("Ingrese el numero de veces que se va a repetir la palabre: "))
            nuevaPalabra = repetidor(palabra, numero)
            print(f"La nueva palabra es: {nuevaPalabra}")
        case 3:
            cont = 0
            palabraLetras = input("Ingrese una palabra: ")
            letra = input("Ingrese la letra para ver cuantas veces se repite: ")
            palabraLetrasLista = list(palabraLetras)
            numero = letraVeces(palabraLetrasLista, letra, cont)
            print(f"La letra {letra} se repite: {numero}")
        case 4:
            numero = int(input("Ingrese el numero para convertirlo en decimal: "))

        case 5:
            contDIgitos = 0
            digitos = int(input("Ingrese el numero para contar sus digitos: "))
            x = contarDigitos(digitos, 1, contDIgitos)
            print(x)
