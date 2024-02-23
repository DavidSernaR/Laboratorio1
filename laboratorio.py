class Conjunto:
    def __init__(self, elementos=None):
        if elementos is None:
            elementos = []
        self.elementos = set(elementos)

    def agregar(self, elemento):
        self.elementos.add(elemento)

    def union(self, otro_conjunto):
        union = Conjunto(self.elementos)
        for elemento in otro_conjunto.elementos:
            union.agregar(elemento)
        return union

    def interseccion(self, otro_conjunto):
        interseccion = Conjunto()
        for elemento in self.elementos:
            if elemento in otro_conjunto.elementos:
                interseccion.agregar(elemento)
        return interseccion

    def diferencia(self, otro_conjunto):
        diferencia = Conjunto(self.elementos)
        for elemento in otro_conjunto.elementos:
            if elemento in diferencia.elementos:
                diferencia.elementos.remove(elemento)
        return diferencia

    def complemento(self, universo):
        complemento = Conjunto(universo.elementos)
        for elemento in self.elementos:
            complemento.elementos.discard(elemento)
        return complemento

    def combinacion(self, otro_conjunto):
        combinacion = Conjunto()
        for elemento in self.elementos:
            combinacion.agregar(elemento)
        for elemento in otro_conjunto.elementos:
            combinacion.agregar(elemento)
        return combinacion

    def cardinalidad(self):
        return len(self.elementos)

    def es_subconjunto(self, otro_conjunto):
        return self.elementos.issubset(otro_conjunto.elementos)

    def es_disjunto(self, otro_conjunto):
        return self.interseccion(otro_conjunto).cardinalidad() == 0


def imprimir_menu():
    print("1. Crear nuevo conjunto")
    print("2. Agregar elemento a un conjunto")
    print("3. Realizar operaciones entre conjuntos")
    print("4. Salir")


def crear_conjunto():
    elementos = input("Ingrese los elementos separados por coma: ").split(",")
    conjunto = Conjunto(elementos)
    return conjunto


def agregar_elemento(conjunto):
    elemento = input("Ingrese el elemento a agregar: ")
    conjunto.agregar(elemento)


def obtener_conjuntos_para_operaciones(conjuntos):
    print("Conjuntos disponibles:")
    for i, conjunto in enumerate(conjuntos):
        print(f"{i + 1}. {conjunto.elementos}")
    indices_conjuntos = input("Seleccione los conjuntos a utilizar separados por coma (por ejemplo, '1,2,3'): ")
    indices = [int(index.strip()) - 1 for index in indices_conjuntos.split(",")]
    conjuntos_seleccionados = [conjuntos[index] for index in indices]
    return conjuntos_seleccionados


def realizar_operaciones(conjuntos):
    print("Operaciones disponibles:")
    print("1. Unión")
    print("2. Intersección")
    print("3. Diferencia")
    print("4. Complemento")
    print("5. Combinación")
    operacion = int(input("Seleccione la operación a realizar: "))

    if operacion == 4:
        print("Conjuntos disponibles:")
        for i, conjunto in enumerate(conjuntos):
            print(f"{i + 1}. {conjunto.elementos}")
        indice_conjunto = int(input("Seleccione el conjunto para el complemento: ")) - 1
        conjunto_seleccionado = conjuntos[indice_conjunto]
        conjunto_universal = Conjunto()
        for conjunto in conjuntos:
            conjunto_universal = conjunto_universal.union(conjunto)
        resultado = conjunto_seleccionado.complemento(conjunto_universal)
    else:
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
    conjunto1, conjunto2, conjunto3 = conjuntos_seleccionados[0], conjuntos_seleccionados[1], conjuntos_seleccionados[2]
    resultado_previo = realizar_operacion_dos_conjuntos(operacion, [conjunto1, conjunto2])
    if resultado_previo:
        return realizar_operacion_dos_conjuntos(operacion, [resultado_previo, conjunto3])
    else:
        return None


def main():
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
            break
        else:
            print("Opción no válida")


if __name__ == "__main__":
    main()
