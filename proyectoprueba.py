import itertools

# Función diferencia
def diferencia(conjunto1, conjunto2):
    return list(set(conjunto1) - set(conjunto2))

# Función diferencia simétrica
def diferencia_simetrica(conjunto1, conjunto2):
    return list(set(conjunto1).symmetric_difference(set(conjunto2)))

# Función unión
def union(conjunto1, conjunto2):
    return list(set(conjunto1) | set(conjunto2))

def convert_to_type(s):
    try:
        return int(s)
    except ValueError:
        try:
            return float(s)
        except ValueError:
            return s

# Función intersección
def obtener_interseccion(conjunto1, conjunto2):
    # Calculamos y devolvemos la intersección de dos conjuntos
    return conjunto1 & conjunto2

def mostrar_resultados(conjunto1, conjunto2, interseccion):
    # Imprime los conjuntos y su intersección
    print("\nEl primer conjunto es:", conjunto1)
    print("El segundo conjunto es:", conjunto2)
    print("\nLa intersección de los dos conjuntos es:", interseccion)

# Función conjunto potencia
def conjunto_potencia(conjunto):
    # Calcula el conjunto potencia de un solo conjunto.
    potencia = []
    for r in range(len(conjunto) + 1):
        for subset in itertools.combinations(conjunto, r):
            potencia.append(set(subset))
    return potencia

def conjunto_potencia_multiple(*conjuntos):
    # Calcula el conjunto potencia de cada conjunto dado.
    resultados = []
    for conjunto in conjuntos:
        resultados.append(conjunto_potencia(conjunto))
    return resultados

# PANTALLA PRINCIPAL
def main():
    print("Bienvenido al proyecto de Estructuras Discretas")
    
    # Ingreso de los conjuntos
    conjunto1 = set(map(convert_to_type, input("Ingrese los elementos del primer conjunto separados por espacios: ").split()))
    conjunto2 = set(map(convert_to_type, input("Ingrese los elementos del segundo conjunto separados por espacios: ").split()))
    
    while True:
        # Menú de opciones
        print("\nMenú de opciones:")
        print("1. Conjunto potencia")
        print("2. Intersección")
        print("3. Unión")
        print("4. Diferencia")
        print("5. Diferencia Simétrica")
        print("6. Salir")
        
        # Elección del usuario
        opcion = input("Seleccione una opción (1-6): ")
        
        if opcion == '1':
            print("Opción seleccionada: Conjunto potencia")
            potencias = conjunto_potencia_multiple(conjunto1, conjunto2)
            print("\nConjunto Potencia de conjunto1:")
            print(potencias[0])
            print("\nConjunto Potencia de conjunto2:")
            print(potencias[1])
            
        elif opcion == '2':
            print("Opción seleccionada: Intersección")
            interseccion = obtener_interseccion(conjunto1, conjunto2)
            mostrar_resultados(conjunto1, conjunto2, interseccion)
            
        elif opcion == '3':
            print("Opción seleccionada: Unión")
            resultado = union(conjunto1, conjunto2)
            print("\nLa unión de los conjuntos es:")
            print(resultado)
            
        elif opcion == '4':
            print("Opción seleccionada: Diferencia")
            resultado = diferencia(conjunto1, conjunto2)
            print("\nLa diferencia del primer conjunto menos el segundo conjunto es:")
            print(resultado)
        
        elif opcion == '5':
            print("Opción seleccionada: Diferencia Simétrica")
            resultado = diferencia_simetrica(conjunto1, conjunto2)
            print("\nLa diferencia simétrica entre los conjuntos es:")
            print(resultado)
        
        elif opcion == '6':
            print("Saliendo del programa...")
            break  # Salir del bucle
        
        else:
            print("Opción no válida. Por favor, elija una opción del 1 al 6.")

if __name__ == "__main__":
    main()


