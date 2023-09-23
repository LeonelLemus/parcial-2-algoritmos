def contar_letra_en_string(frase, letra):
    frase = frase.lower()
    letra = letra.lower()

    cantidad = frase.count(letra)
    
    return cantidad

frase_ingresada = input("Ingrese una frase en mayúsculas o minúsculas: ")
letra_ingresada = input("Ingrese una letra: ")

resultado = contar_letra_en_string(frase_ingresada, letra_ingresada)
print(f"La letra '{letra_ingresada}' aparece {resultado} veces en la frase.")
