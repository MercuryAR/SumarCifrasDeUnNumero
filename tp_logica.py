print("Bienvenidos al TP de Logica - Tema 6")
print("Alumnos Paulo Orsini")
print("Comisión 9 - Año 2026")
print()
print("Este programa calcula la suma de las cifras de un numero entero.")
print()

#Declaro la función resolver que recibe un parámetro n (número)
def resolver(n):
    # Se refuerza el control y validación de errores incluyendo este condicional dentro de la función
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("Error: el parámetro debe ser un número entero válido.")

    if n < 0:
        raise ValueError("Error: el número no puede ser negativo.")

    suma = 0
    while n > 0:
        digito = n % 10
        suma = suma + digito
        n = n // 10
    return suma

# Programa principal
entrada_válida = False

while entrada_válida == False:
    print("Ingresá un número entero mayor o igual a cero: ")
    entrada = input()

    try:
        # Primer control: rechaza entrada con signo + explícito
        if entrada.strip().startswith('+'):
            print("Error: no se aceptan números con signo + explícito.")
            continue

        numero = int(entrada)
        if numero < 0:
            print("Error: el número no puede ser negativo.")
        else:
            # Segundo control: validación dentro de la función resolver()
            resultado = resolver(numero)
            entrada_válida = True

    except ValueError:
        print("Error: el valor ingresado no es un número entero válido.")
    except (TypeError, ValueError) as e:
        print(str(e))

if entrada_válida:
    print(f"La suma de las cifras de {numero} es: {resultado}")
