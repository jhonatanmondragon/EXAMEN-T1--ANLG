

import random


def crearEntrenador(tupla):
    
    print("\n--- Crear Entrenador ---")
    nombre_entrenador = input("Nombre del entrenador: ")
    nombre_pokemon = input("Nombre del pokemon: ")

    ataque = random.randint(150, 250)
    vida = random.randint(500, 900)

    tupla.append((nombre_entrenador, nombre_pokemon, ataque, vida))

    print(f"Se registró a {nombre_entrenador} con {nombre_pokemon} "
          f"(Ataque: {ataque}, Vida: {vida})\n")


def listaEntrenador(tupla):
    
    n = len(tupla)

    if n == 0:
        print("\nNo hay entrenadores registrados todavía.\n")
        return

    # --- Ordenamiento burbuja por ataque (de mayor a menor) ---
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if tupla[j][2] < tupla[j + 1][2]:
                tupla[j], tupla[j + 1] = tupla[j + 1], tupla[j]

    print("\n--- Lista de Entrenadores (ordenado por ataque) ---")
    print(f"{'N°':<4}{'Entrenador':<15}{'Pokemon':<15}{'Ataque':<10}{'Vida':<10}")
    for indice in range(n):
        entrenador, pokemon, ataque, vida = tupla[indice]
        print(f"{indice + 1:<4}{entrenador:<15}{pokemon:<15}{ataque:<10}{vida:<10}")
    print()


def borraPorPokemon(tupla):
    
    n = len(tupla)

    if n == 0:
        print("\nNo hay entrenadores registrados para borrar.\n")
        return

    # --- Ordenamiento por selección, por vida (de menor a mayor) ---
    for i in range(n - 1):
        menor = i
        for j in range(i + 1, n):
            if tupla[j][3] < tupla[menor][3]:
                menor = j
        tupla[i], tupla[menor] = tupla[menor], tupla[i]

    try:
        vida_buscada = int(input("Ingrese la vida del pokemon a borrar: "))
    except ValueError:
        print("\nDebe ingresar un número.\n")
        return

    # --- Búsqueda binaria sobre la lista ya ordenada por vida ---
    izquierda, derecha = 0, n - 1
    posicion = -1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if tupla[medio][3] == vida_buscada:
            posicion = medio
            break
        elif tupla[medio][3] < vida_buscada:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    if posicion == -1:
        print(f"\nNo se encontró ningún pokemon con vida {vida_buscada}.\n")
    else:
        entrenador, pokemon, ataque, vida = tupla[posicion]
        del tupla[posicion]
        print(f"\nSe eliminó a {entrenador} y su pokemon {pokemon} (vida: {vida}).\n")


def peleaPokemon(lista):
   
    listaEntrenador(lista)
    n = len(lista)

    if n < 2:
        print("Se necesitan al menos 2 entrenadores para pelear.\n")
        return

    try:
        num1 = int(input("Número del primer pokemon: "))
        num2 = int(input("Número del segundo pokemon: "))
    except ValueError:
        print("\nDebe ingresar números válidos.\n")
        return

    if not (1 <= num1 <= n) or not (1 <= num2 <= n) or num1 == num2:
        print("\nNúmeros inválidos.\n")
        return

    idx1, idx2 = num1 - 1, num2 - 1
    entrenador1, pokemon1, ataque1, vida1 = lista[idx1]
    entrenador2, pokemon2, ataque2, vida2 = lista[idx2]

    dano_a_2 = ataque1 * random.randint(0, 5)
    dano_a_1 = ataque2 * random.randint(0, 5)

    vidaFinal1 = vida1 - dano_a_1
    vidaFinal2 = vida2 - dano_a_2

    print(f"\n{pokemon1} ({entrenador1}) ataca causando {dano_a_2} de daño.")
    print(f"{pokemon2} ({entrenador2}) ataca causando {dano_a_1} de daño.")
    print(f"Vida restante de {pokemon1}: {vidaFinal1}")
    print(f"Vida restante de {pokemon2}: {vidaFinal2}")

    def borrarAmbos():
        # Se borra primero el índice mayor para no desordenar al otro
        if idx1 > idx2:
            del lista[idx1]
            del lista[idx2]
        else:
            del lista[idx2]
            del lista[idx1]

    if vidaFinal1 <= 0 and vidaFinal2 <= 0:
        print(f"\n¡Ambos pokemon quedaron sin vida! {entrenador1} y {entrenador2} pierden.\n")
        borrarAmbos()
    elif vidaFinal1 == vidaFinal2:
        print(f"\n¡Empate! {entrenador1} y {entrenador2} pierden ambos.\n")
        borrarAmbos()
    elif vidaFinal1 > vidaFinal2:
        print(f"\n¡Gana {entrenador1} con {pokemon1}!\n")
        del lista[idx2]
    else:
        print(f"\n¡Gana {entrenador2} con {pokemon2}!\n")
        del lista[idx1]


def menu():
    entrenadores = []

    while True:
        print("========= MENU POKEMON =========")
        print("1. Crear Entrenador")
        print("2. Listar Entrenadores")
        print("3. Borrar por Pokemon")
        print("4. Pelea Pokemon")
        print("5. Fin")

        opcion = input("Elija una opción: ")

        if opcion == "1":
            crearEntrenador(entrenadores)
        elif opcion == "2":
            listaEntrenador(entrenadores)
        elif opcion == "3":
            borraPorPokemon(entrenadores)
        elif opcion == "4":
            peleaPokemon(entrenadores)
        elif opcion == "5":
            print("\n¡Hasta luego, entrenador!")
            break
        else:
            print("\nOpción inválida, intente nuevamente.\n")


if __name__ == "__main__":
    menu()