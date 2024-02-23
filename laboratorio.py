class Conjunto:
    def __init__(self, elementos=None):
        # Constructor de la clase Conjunto.
        # Inicializa un conjunto con los elementos proporcionados.
        if elementos is None:
            elementos = []
        self.elementos = set(elementos)

    def agregar(self, elemento):
        # Método para agregar un elemento al conjunto.
        self.elementos.add(elemento)

    def union(self, otro_conjunto):
        # Método para realizar la operación de unión entre dos conjuntos.
        # Crea un nuevo conjunto que contiene los elementos de ambos conjuntos.
        union = Conjunto(self.elementos)
        for elemento in otro_conjunto.elementos:
            union.agregar(elemento)
        return union

    def interseccion(self, otro_conjunto):
        # Método para realizar la operación de intersección entre dos conjuntos.
        # Crea un nuevo conjunto que contiene los elementos comunes a ambos conjuntos.
        interseccion = Conjunto()
        for elemento in self.elementos:
            if elemento in otro_conjunto.elementos:
                interseccion.agregar(elemento)
        return interseccion

    def diferencia(self, otro_conjunto):
        # Método para realizar la operación de diferencia entre dos conjuntos.
        # Crea un nuevo conjunto que contiene los elementos del primer conjunto que no están en el segundo.
        diferencia = Conjunto(self.elementos)
        for elemento in otro_conjunto.elementos:
            if elemento in diferencia.elementos:
                diferencia.elementos.remove(elemento)
        return diferencia

    def complemento(self, universo):
        # Método para calcular el complemento de un conjunto.
        # El complemento se define como los elementos del conjunto universal que no están en el conjunto.
        complemento = Conjunto(universo.elementos)
        for elemento in self.elementos:
            complemento.elementos.discard(elemento)
        return complemento

    def combinacion(self, otro_conjunto):
        # Método para realizar la operación de combinación entre dos conjuntos.
        # Crea un nuevo conjunto que contiene todos los elementos de ambos conjuntos.
        combinacion = Conjunto()
        for elemento in self.elementos:
            combinacion.agregar(elemento)
        for elemento in otro_conjunto.elementos:
            combinacion.agregar(elemento)
        return combinacion

    def cardinalidad(self):
        # Método para calcular la cardinalidad (cantidad de elementos) del conjunto.
        return len(self.elementos)

    def es_subconjunto(self, otro_conjunto):
        # Método para verificar si el conjunto es un subconjunto de otro.
        return self.elementos.issubset(otro_conjunto.elementos)

    def es_disjunto(self, otro_conjunto):
        # Método para verificar si dos conjuntos son disjuntos (no tienen elementos en común).
        return self.interseccion(otro_conjunto).cardinalidad() == 0


def imprimir_menu():
    # Función para imprimir el menú de opciones.
    print("1. Crear nuevo conjunto")
    print("2. Agregar elemento a un conjunto")
    print("3. Realizar operaciones entre conjuntos")
    print("4. Conocer la cardinalidad de un conjunto")
    print("5. Verificar si un conjunto es subconjunto de otro")
    print("6. Verificar si dos conjuntos son disyuntos")
    print("7. Salir")

def obtener_indice_conjunto(conjuntos):
    # Función para obtener el índice del conjunto seleccionado por el usuario.
    print("Conjuntos disponibles:")
    for i, conjunto in enumerate(conjuntos):
        print(f"{i + 1}. {conjunto.elementos}")
    return int(input("Seleccione el número del conjunto: ")) - 1

def conocer_cardinalidad(conjuntos):
    # Función para conocer la cardinalidad de un conjunto.
    indice_conjunto = obtener_indice_conjunto(conjuntos)
    conjunto_seleccionado = conjuntos[indice_conjunto]
    print("La cardinalidad del conjunto es:", conjunto_seleccionado.cardinalidad())

def verificar_subconjunto(conjuntos):
    # Función para verificar si un conjunto es subconjunto de otro.
    print("Seleccione el primer conjunto:")
    indice_conjunto1 = obtener_indice_conjunto(conjuntos)
    print("Seleccione el segundo conjunto:")
    indice_conjunto2 = obtener_indice_conjunto(conjuntos)
    conjunto1 = conjuntos[indice_conjunto1]
    conjunto2 = conjuntos[indice_conjunto2]
    if conjunto1.es_subconjunto(conjunto2):
        print("El primer conjunto es subconjunto del segundo.")
    else:
        print("El primer conjunto NO es subconjunto del segundo.")

def verificar_disyuntos(conjuntos):
    # Función para verificar si dos conjuntos son disyuntos.
    print("Seleccione el primer conjunto:")
    indice_conjunto1 = obtener_indice_conjunto(conjuntos)
    print("Seleccione el segundo conjunto:")
    indice_conjunto2 = obtener_indice_conjunto(conjuntos)
    conjunto1 = conjuntos[indice_conjunto1]
    conjunto2 = conjuntos[indice_conjunto2]
    if conjunto1.es_disjunto(conjunto2):
        print("Los conjuntos son disyuntos.")
    else:
        print("Los conjuntos NO son disyuntos.")


def crear_conjunto():
    # Función para crear un nuevo conjunto ingresando elementos desde la entrada estándar.
    elementos = input("Ingrese los elementos separados por coma: ").split(",")
    conjunto = Conjunto(elementos)
    return conjunto


def agregar_elemento(conjunto):
    # Función para agregar un elemento a un conjunto existente.
    elemento = input("Ingrese el elemento a agregar: ")
    conjunto.agregar(elemento)


def obtener_conjuntos_para_operaciones(conjuntos):
    # Función para obtener los conjuntos seleccionados por el usuario para realizar operaciones.
    print("Conjuntos disponibles:")
    for i, conjunto in enumerate(conjuntos):
        print(f"{i + 1}. {conjunto.elementos}")
    indices_conjuntos = input("Seleccione los conjuntos a utilizar separados por coma (por ejemplo, '1,2,3'): ")
    indices = [int(index.strip()) - 1 for index in indices_conjuntos.split(",")]
    conjuntos_seleccionados = [conjuntos[index] for index in indices]
    return conjuntos_seleccionados


def realizar_operaciones(conjuntos):
    # Función para realizar operaciones entre conjuntos.
    print("Operaciones disponibles:")
    print("1. Unión")
    print("2. Intersección")
    print("3. Diferencia")
    print("4. Complemento")
    print("5. Combinación")
    operacion = int(input("Seleccione la operación a realizar: "))

    if operacion == 4:
        # Si la operación es complemento, se solicita al usuario que seleccione un conjunto.
        print("Conjuntos disponibles:")
        for i, conjunto in enumerate(conjuntos):
            print(f"{i + 1}. {conjunto.elementos}")
        indice_conjunto = int(input("Seleccione el conjunto para el complemento: ")) - 1
        conjunto_seleccionado = conjuntos[indice_conjunto]
        # Se crea el conjunto universal, que es la unión de todos los conjuntos.
        conjunto_universal = Conjunto()
        for conjunto in conjuntos:
            conjunto_universal = conjunto_universal.union(conjunto)
        # Se calcula el complemento del conjunto seleccionado utilizando el conjunto universal.
        resultado = conjunto_seleccionado.complemento(conjunto_universal)
    else:
        # Para otras operaciones, se obtienen los conjuntos seleccionados por el usuario.
        conjuntos_seleccionados = obtener_conjuntos_para_operaciones(conjuntos)
        if len(conjuntos_seleccionados) == 2:
            resultado = realizar_operacion_dos_conjuntos(operacion, conjuntos_seleccionados)
        elif len(conjuntos_seleccionados) == 3:
            resultado = realizar_operacion_tres_conjuntos(operacion, conjuntos_seleccionados)
        else:
            print("Operación no válida")
            return

    print("Resultado:", resultado.elementos)


def realizar_operacion_dos_conjuntos(operacion, conjuntos_seleccionados):
    # Función para realizar operaciones entre dos conjuntos.
    conjunto1, conjunto2 = conjuntos_seleccionados[0], conjuntos_seleccionados[1]
    if operacion == 1:
        return conjunto1.union(conjunto2)
    elif operacion == 2:
        return conjunto1.interseccion(conjunto2)
    elif operacion == 3:
        return conjunto1.diferencia(conjunto2)
    elif operacion == 5:
        return conjunto1.combinacion(conjunto2)
    else:
        return None


def realizar_operacion_tres_conjuntos(operacion, conjuntos_seleccionados):
    # Función para realizar operaciones entre tres conjuntos.
    conjunto1, conjunto2, conjunto3 = conjuntos_seleccionados[0], conjuntos_seleccionados[1], conjuntos_seleccionados[2]
    resultado_previo = realizar_operacion_dos_conjuntos(operacion, [conjunto1, conjunto2])
    if resultado_previo:
        return realizar_operacion_dos_conjuntos(operacion, [resultado_previo, conjunto3])
    else:
        return None


def main():
    # Función principal que controla el flujo del programa.
    conjuntos = []
    while True:
        imprimir_menu()
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            conjuntos.append(crear_conjunto())
        elif opcion == 2:
            if len(conjuntos) == 0:
                print("No hay conjuntos creados. Cree un conjunto primero.")
            else:
                print("Seleccione un conjunto:")
                for i, conjunto in enumerate(conjuntos):
                    print(f"{i + 1}. {conjunto.elementos}")
                indice_conjunto = int(input()) - 1
                agregar_elemento(conjuntos[indice_conjunto])
        elif opcion == 3:
            if len(conjuntos) < 2:
                print("Se necesitan al menos dos conjuntos para realizar operaciones.")
            else:
                realizar_operaciones(conjuntos)
        elif opcion == 4:
            if len(conjuntos) == 0:
                print("No hay conjuntos creados. Cree un conjunto primero.")
            else:
                conocer_cardinalidad(conjuntos)
        elif opcion == 5:
            if len(conjuntos) < 2:
                print("Se necesitan al menos dos conjuntos para verificar subconjuntos.")
            else:
                verificar_subconjunto(conjuntos)
        elif opcion == 6:
            if len(conjuntos) < 2:
                print("Se necesitan al menos dos conjuntos para verificar si son disyuntos.")
            else:
                verificar_disyuntos(conjuntos)
        elif opcion == 7:
            break
        else:
            print("Opción no válida")


if __name__ == "__main__":
    main()
