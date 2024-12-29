""""calculadora"""

print("Bienvenido a esta calculadora para realizar operaciones básicas")

while True:
    n1 = input("ingresa un primer número: ")
    n2 = input("ingresa un segundo número: ")
    try:
        n1 = int(n1)
        n2 = int(n2)
    except ValueError:
        print("Por favor, ingresa números válidos.")
        continue

    n3 = (
        input("ingresa la operación deseada(suma, resta, multiplicación, división)")
        .strip()
        .lower()
    )

    if n3 == "suma":
        print(f"resultado: {n1 + n2}")
    elif n3 == "resta":
        print(f"resultado: {n1 - n2}")
    elif n3 == "multiplicacion" or n3 == "multiplicación":
        print(f"resultado: {n1 * n2}")
    elif n3 == "division" or n3 == "división":
        if n2 != 0:
            print(f"resultado: {n1 / n2}")
        else:
            print("no se puede dividir entre 0")
    else:
        print("No se puede realizar la operación")
        continue

    repetir = input("¿Deseas realizar otra operación? (sí/no): ").strip().lower()
    if repetir == "sí" or repetir == "si":
        print("¡Continuemos!")
    else:
        print("¡Hasta luego!")
        break
