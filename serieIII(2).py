import sys

def calcular_suma(valores):
    return sum(valores)

def calcular_promedio(valores):
    if len(valores) == 0:
        return 0
    return sum(valores) / len(valores)

def main():
    if len(sys.argv) < 2:
        print("Debes proporcionar valores separados por comas como argumento.")
        return

    valores_str = sys.argv[1].split(',')
    valores = [float(valor) for valor in valores_str]

    suma = calcular_suma(valores)
    promedio = calcular_promedio(valores)

    print(f"La suma es {suma}, promedio es {promedio:.2f}")

if __name__ == "__main__":
    main()
