# Universidad del Quindío
# Asignatura: Teoría de Lenguajes Formales
# Docente: Ana María Tamayo Ocampo
# Integrantes: Esteban Julián Ortega Tapie y David Serna Restrepo

# Solución de Laboratorio sobre la Teoría de Conjuntos

# Abstracción: Es simplificar y enfocarse en lo esencial de un problema, ignorando los detalles innecesarios.
# Descomposición: Implica dividir un problema complejo en partes más pequeñas y manejables para entenderlo mejor y resolverlo de manera más efectiva.
# Codificación: Es expresar una solución o algoritmo en un lenguaje de programación, utilizando una sintaxis específica, para que una computadora pueda entender y ejecutar las instrucciones correspondientes.

import tkinter as tk # Abstracción: Importación de la biblioteca Tkinter para la interfaz gráfica
from tkinter import messagebox # Abstracción: Importación específica de la clase messagebox para mostrar mensajes emergentes
import matplotlib.pyplot as plt # Abstracción: Importación de la biblioteca Matplotlib para gráficos
from matplotlib_venn import venn2, venn2_circles, venn3, venn3_circles # Abstracción: Importación de funciones específicas de Matplotlib para diagramas de Venn

class Conjunto:
    # Abstracción: Definición de la clase Conjunto para representar conjuntos y realizar operaciones con ellos
    # Descomposición: Métodos específicos para realizar operaciones comunes con conjuntos como unión, intersección, diferencia, etc.

    # Constructor de la clase Conjunto
    # Reconocimiento de patrones: Inicializa un conjunto con los elementos proporcionados
    def _init_(self, elementos=None):
        if elementos is None:
            elementos = []
        self.elementos = set(elementos)

    # Método para agregar un elemento al conjunto
    def agregar(self, elemento):
        self.elementos.add(elemento)

    # Métodos para realizar operaciones entre conjuntos (unión, intersección, diferencia, complemento, combinación)
    
    # Abstracción: Cada método encapsula la lógica de una operación específica

    # Método para realizar la operación de unión entre dos conjuntos
    # Crea un nuevo conjunto que contiene los elementos de ambos conjuntos
    def union(self, otro_conjunto):
        union = Conjunto(self.elementos)
        for elemento in otro_conjunto.elementos:
            union.agregar(elemento)
        return union

    # Método para realizar la operación de intersección entre dos conjuntos
    # Crea un nuevo conjunto que contiene los elementos comunes a ambos conjuntos
    def interseccion(self, otro_conjunto):
        interseccion = Conjunto()
        for elemento in self.elementos:
            if elemento in otro_conjunto.elementos:
                interseccion.agregar(elemento)
        return interseccion

    # Método para realizar la operación de diferencia entre dos conjuntos
    # Crea un nuevo conjunto que contiene los elementos del primer conjunto que no están en el segundo
    def diferencia(self, otro_conjunto):
        diferencia = Conjunto(self.elementos)
        for elemento in otro_conjunto.elementos:
            if elemento in diferencia.elementos:
                diferencia.elementos.remove(elemento)
        return diferencia

    # Método para calcular el complemento de un conjunto
    # Codificación: El complemento se define como los elementos del conjunto universal que no están en el conjunto
    # Crea un nuevo conjunto que contiene todos los elementos de ambos conjuntos y luego se descarta los elementos del conjunto seleccionado
    def complemento(self, universo):
        complemento = Conjunto(universo.elementos)
        for elemento in self.elementos:
            complemento.elementos.discard(elemento)
        return complemento

    # Método para realizar la operación de combinación entre dos conjuntos
    # Crea un nuevo conjunto que contiene todos los elementos de ambos conjuntos
    def combinacion(self, otro_conjunto):
        combinacion = Conjunto()
        for elemento in self.elementos:
            combinacion.agregar(elemento)
        for elemento in otro_conjunto.elementos:
            combinacion.agregar(elemento)
        return combinacion

    # Método para calcular la cardinalidad (cantidad de elementos) del conjunto
    def cardinalidad(self):
        return len(self.elementos)

    # Método para verificar si el conjunto es un subconjunto de otro
    def es_subconjunto(self, otro_conjunto):
        return self.elementos.issubset(otro_conjunto.elementos)

    # Método para verificar si dos conjuntos son disjuntos (no tienen elementos en común).
    def es_disjunto(self, otro_conjunto):
        return self.interseccion(otro_conjunto).cardinalidad() == 0

# Método para crear la ventana principal
def crear_ventana_principal():
    ventana = tk.Tk()
    ventana.title("Operaciones entre conjuntos")

    # Marco principal
    marco_principal = tk.Frame(ventana)
    marco_principal.pack(padx=10, pady=10)

    # Etiqueta de instrucciones
    lbl_instrucciones = tk.Label(marco_principal, text="Seleccione una opción:")
    lbl_instrucciones.grid(row=0, column=0, columnspan=2, pady=(0, 10))

    # Botones para las diferentes operaciones
    # Abstracción: Cada botón representa una opción de operación entre conjuntos
    # Descomposición: Los botones están organizados en una cuadrícula dentro del marco principal
    btn_opciones = [
        ("Crear nuevo conjunto", crear_nuevo_conjunto),
        ("Agregar elemento a un conjunto", agregar_elemento_conjunto),
        ("Realizar operaciones entre conjuntos", realizar_operaciones),
        ("Conocer la cardinalidad de un conjunto", conocer_cardinalidad),
        ("Verificar si un conjunto es subconjunto de otro", verificar_subconjunto),
        ("Verificar si dos conjuntos son disyuntos", verificar_disyuntos),
        ("Complemento", calcular_complemento),
        ("Salir", ventana.quit)
    ]

    for i, (text, comando) in enumerate(btn_opciones, start=1):
        btn = tk.Button(marco_principal, text=text, width=30, command=comando)
        btn.grid(row=i, column=0, pady=5)

    return ventana

# Método para crear un nuevo conjunto
def crear_nuevo_conjunto():
    ventana_nuevo_conjunto = tk.Toplevel()
    ventana_nuevo_conjunto.title("Crear nuevo conjunto")

    # Cuadro de entrada para los elementos del conjunto
    lbl_instrucciones = tk.Label(ventana_nuevo_conjunto, text="Ingrese los elementos separados por coma:")
    lbl_instrucciones.pack(pady=(10, 5))
    entrada_elementos = tk.Entry(ventana_nuevo_conjunto)
    entrada_elementos.pack(pady=5)

    # Función para agregar un nuevo conjunto a la lista de conjuntos
    def agregar_conjunto():
        elementos = entrada_elementos.get().split(",")
        conjuntos.append(Conjunto(elementos))
        ventana_nuevo_conjunto.destroy()
        messagebox.showinfo("Éxito", "Conjunto creado exitosamente.")

    # Botón para agregar el conjunto
    btn_agregar = tk.Button(ventana_nuevo_conjunto, text="Agregar conjunto", command=agregar_conjunto)
    btn_agregar.pack(pady=5)

# Método para agregar un nuevo elemento a un conjunto en específico
def agregar_elemento_conjunto():
    ventana_agregar_elemento = tk.Toplevel()
    ventana_agregar_elemento.title("Agregar elemento a un conjunto")

    # Menú desplegable para seleccionar el conjunto al que se agregará el elemento
    lbl_conjunto = tk.Label(ventana_agregar_elemento, text="Seleccione el conjunto:")
    lbl_conjunto.pack(pady=(10, 5))
    seleccion_conjunto = tk.StringVar()
    seleccion_conjunto.set("Seleccionar conjunto")
    menu_conjunto = tk.OptionMenu(ventana_agregar_elemento, seleccion_conjunto, *[(i + 1) for i in range(len(conjuntos))])
    menu_conjunto.pack(pady=5)

    # Cuadro de entrada para el nuevo elemento
    lbl_elemento = tk.Label(ventana_agregar_elemento, text="Ingrese el elemento a agregar:")
    lbl_elemento.pack(pady=(10, 5))
    entrada_elemento = tk.Entry(ventana_agregar_elemento)
    entrada_elemento.pack(pady=5)

    # Función para agregar el elemento al conjunto seleccionado
    def agregar_elemento():
        try:
            indice_conjunto = int(seleccion_conjunto.get()) - 1
            elemento = entrada_elemento.get()
            conjuntos[indice_conjunto].agregar(elemento)
            ventana_agregar_elemento.destroy()
            messagebox.showinfo("Éxito", f"Elemento '{elemento}' agregado al conjunto.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    # Botón para agregar el elemento
    btn_agregar = tk.Button(ventana_agregar_elemento, text="Agregar elemento", command=agregar_elemento)
    btn_agregar.pack(pady=5)

# Método para realizar las operaciones
def realizar_operaciones():
    ventana_operaciones = tk.Toplevel()
    ventana_operaciones.title("Realizar operaciones entre conjuntos")

    # Menú desplegable para seleccionar el primer conjunto
    lbl_conjunto1 = tk.Label(ventana_operaciones, text="Seleccione el primer conjunto:")
    lbl_conjunto1.pack(pady=(10, 5))
    seleccion_conjunto1 = tk.StringVar()
    seleccion_conjunto1.set("Seleccionar conjunto")
    menu_conjunto1 = tk.OptionMenu(ventana_operaciones, seleccion_conjunto1, *[(i + 1) for i in range(len(conjuntos))])
    menu_conjunto1.pack(pady=5)

    # Menú desplegable para seleccionar el segundo conjunto
    lbl_conjunto2 = tk.Label(ventana_operaciones, text="Seleccione el segundo conjunto:")
    lbl_conjunto2.pack(pady=(10, 5))
    seleccion_conjunto2 = tk.StringVar()
    seleccion_conjunto2.set("Seleccionar conjunto")
    menu_conjunto2 = tk.OptionMenu(ventana_operaciones, seleccion_conjunto2, *[(i + 1) for i in range(len(conjuntos))])
    menu_conjunto2.pack(pady=5)

    # Menú desplegable para seleccionar la operación
    lbl_operacion = tk.Label(ventana_operaciones, text="Seleccione la operación:")
    lbl_operacion.pack(pady=(10, 5))
    seleccion_operacion = tk.StringVar()
    seleccion_operacion.set("")
    menu_operacion = tk.OptionMenu(ventana_operaciones, seleccion_operacion, "Unión", "Intersección", "Diferencia", "Combinación")
    menu_operacion.pack(pady=5)

    # Función para realizar la operación seleccionada
    def realizar_operacion():
        try:
            indice_conjunto1 = int(seleccion_conjunto1.get()) - 1
            indice_conjunto2 = int(seleccion_conjunto2.get()) - 1
            operacion = seleccion_operacion.get()

            conjunto1 = conjuntos[indice_conjunto1]
            conjunto2 = conjuntos[indice_conjunto2]

            resultado = None

            if operacion == "Unión":
                resultado = conjunto1.union(conjunto2)
            elif operacion == "Intersección":
                resultado = conjunto1.interseccion(conjunto2)
            elif operacion == "Diferencia":
                resultado = conjunto1.diferencia(conjunto2)
            elif operacion == "Combinación":
                resultado = conjunto1.combinacion(conjunto2)

            messagebox.showinfo("Resultado", f"El resultado de la operación es: {resultado.elementos}")
            mostrar_diagrama_venn([conjunto1, conjunto2, resultado], operacion)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    # Botón para realizar la operación
    btn_realizar_operacion = tk.Button(ventana_operaciones, text="Realizar operación", command=realizar_operacion)
    btn_realizar_operacion.pack(pady=5)

# Método para conocer la cardinalidad de un conjunto
def conocer_cardinalidad():
    ventana_cardinalidad = tk.Toplevel()
    ventana_cardinalidad.title("Conocer la cardinalidad de un conjunto")

    # Crear un menú desplegable para seleccionar el conjunto
    lbl_conjunto = tk.Label(ventana_cardinalidad, text="Seleccione el conjunto:")
    lbl_conjunto.pack(pady=(10, 5))
    seleccion_conjunto = tk.StringVar()
    seleccion_conjunto.set("Seleccionar conjunto")
    menu_conjunto = tk.OptionMenu(ventana_cardinalidad, seleccion_conjunto, *[(i + 1) for i in range(len(conjuntos))])
    menu_conjunto.pack(pady=5)

    # Función para mostrar la cardinalidad del conjunto seleccionado
    def mostrar_cardinalidad():
        try:
            indice_conjunto = int(seleccion_conjunto.get()) - 1
            cardinalidad = conjuntos[indice_conjunto].cardinalidad()
            messagebox.showinfo("Cardinalidad", f"La cardinalidad del conjunto es: {cardinalidad}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    # Botón para mostrar la cardinalidad
    btn_mostrar_cardinalidad = tk.Button(ventana_cardinalidad, text="Mostrar cardinalidad", command=mostrar_cardinalidad)
    btn_mostrar_cardinalidad.pack(pady=5)

# Método para verificar si un conjunto es subconjunto de otro
def verificar_subconjunto():
    ventana_verificar_subconjunto = tk.Toplevel()
    ventana_verificar_subconjunto.title("Verificar si un conjunto es subconjunto de otro")

    # Crear menús desplegables para seleccionar los conjuntos
    lbl_conjunto1 = tk.Label(ventana_verificar_subconjunto, text="Seleccione el primer conjunto:")
    lbl_conjunto1.pack(pady=(10, 5))
    seleccion_conjunto1 = tk.StringVar()
    seleccion_conjunto1.set("Seleccionar conjunto")
    menu_conjunto1 = tk.OptionMenu(ventana_verificar_subconjunto, seleccion_conjunto1, *[(i + 1) for i in range(len(conjuntos))])
    menu_conjunto1.pack(pady=5)

    lbl_conjunto2 = tk.Label(ventana_verificar_subconjunto, text="Seleccione el segundo conjunto:")
    lbl_conjunto2.pack(pady=(10, 5))
    seleccion_conjunto2 = tk.StringVar()
    seleccion_conjunto2.set("Seleccionar conjunto")
    menu_conjunto2 = tk.OptionMenu(ventana_verificar_subconjunto, seleccion_conjunto2, *[(i + 1) for i in range(len(conjuntos))])
    menu_conjunto2.pack(pady=5)

    # Función para verificar si el primer conjunto es subconjunto del segundo
    def verificar_subconjunto():
        try:
            indice_conjunto1 = int(seleccion_conjunto1.get()) - 1
            indice_conjunto2 = int(seleccion_conjunto2.get()) - 1
            if conjuntos[indice_conjunto1].es_subconjunto(conjuntos[indice_conjunto2]):
                messagebox.showinfo("Resultado", "El primer conjunto es subconjunto del segundo.")
            else:
                messagebox.showinfo("Resultado", "El primer conjunto NO es subconjunto del segundo.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    # Botón para verificar si el primer conjunto es subconjunto del segundo
    btn_verificar_subconjunto = tk.Button(ventana_verificar_subconjunto, text="Verificar subconjunto", command=verificar_subconjunto)
    btn_verificar_subconjunto.pack(pady=5)

# Método para verificar si dos conjuntos son disjuntos
def verificar_disyuntos():
    ventana_verificar_disyuntos = tk.Toplevel()
    ventana_verificar_disyuntos.title("Verificar si dos conjuntos son disyuntos")

    # Menús desplegables para seleccionar los conjuntos
    lbl_conjunto1 = tk.Label(ventana_verificar_disyuntos, text="Seleccione el primer conjunto:")
    lbl_conjunto1.pack(pady=(10, 5))
    seleccion_conjunto1 = tk.StringVar()
    seleccion_conjunto1.set("Seleccionar conjunto")
    menu_conjunto1 = tk.OptionMenu(ventana_verificar_disyuntos, seleccion_conjunto1, *[(i + 1) for i in range(len(conjuntos))])
    menu_conjunto1.pack(pady=5)

    lbl_conjunto2 = tk.Label(ventana_verificar_disyuntos, text="Seleccione el segundo conjunto:")
    lbl_conjunto2.pack(pady=(10, 5))
    seleccion_conjunto2 = tk.StringVar()
    seleccion_conjunto2.set("Seleccionar conjunto")
    menu_conjunto2 = tk.OptionMenu(ventana_verificar_disyuntos, seleccion_conjunto2, *[(i + 1) for i in range(len(conjuntos))])
    menu_conjunto2.pack(pady=5)

    # Función para verificar si los conjuntos son disjuntos
    def verificar_disyuntos():
        try:
            indice_conjunto1 = int(seleccion_conjunto1.get()) - 1
            indice_conjunto2 = int(seleccion_conjunto2.get()) - 1
            if conjuntos[indice_conjunto1].es_disjunto(conjuntos[indice_conjunto2]):
                messagebox.showinfo("Resultado", "Los conjuntos NO son disyuntos.")
            else:
                messagebox.showinfo("Resultado", "Los conjuntos son disyuntos.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    # Botón para verificar si los conjuntos son disyuntos
    btn_verificar_disyuntos = tk.Button(ventana_verificar_disyuntos, text="Verificar disyuntos", command=verificar_disyuntos)
    btn_verificar_disyuntos.pack(pady=5)

# Método para hallar el complemento de un conjunto
def calcular_complemento():
    ventana_complemento = tk.Toplevel()
    ventana_complemento.title("Calcular el complemento de un conjunto")

    lbl_conjunto = tk.Label(ventana_complemento, text="Seleccione el conjunto:")
    lbl_conjunto.pack(pady=(10, 5))
    seleccion_conjunto = tk.StringVar()
    seleccion_conjunto.set("Seleccionar conjunto")
    menu_conjunto = tk.OptionMenu(ventana_complemento, seleccion_conjunto, *[(i + 1) for i in range(len(conjuntos))])
    menu_conjunto.pack(pady=5)

    # Función para mostrar el complemento de un conjunto seleccionado
    def mostrar_complemento():
        try:
            indice_conjunto = int(seleccion_conjunto.get()) - 1
            universo = Conjunto()
            for conjunto in conjuntos:
                universo = universo.union(conjunto)
            complemento = conjuntos[indice_conjunto].complemento(universo)
            messagebox.showinfo("Complemento", f"El complemento del conjunto es: {complemento.elementos}")
            mostrar_diagrama_venn([conjuntos[indice_conjunto], complemento], "Complemento")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    # Botón para hallar el complemento de un conjunto seleccionado
    btn_mostrar_complemento = tk.Button(ventana_complemento, text="Mostrar complemento", command=mostrar_complemento)
    btn_mostrar_complemento.pack(pady=5)

# Método para mostrar un diagrama de Venn para representar la operación realizada
def mostrar_diagrama_venn(conjuntos, operacion):
        plt.figure(figsize=(6, 6))
        if operacion == "Diferencia":
            venn = venn3([conjuntos[0].elementos, conjuntos[1].elementos, conjuntos[2].elementos], set_labels=('Conjunto 1', 'Conjunto 2', 'Resultado'))
            # Obtener los números de cada conjunto
            numeros_conjunto1 = ", ".join(map(str, conjuntos[1].diferencia(conjuntos[0]).elementos))
            numeros_conjunto2 = ", ".join(map(str, conjuntos[0].diferencia(conjuntos[1]).elementos))
            # Obtener los números de la intersección
            interseccion_12 = ", ".join(map(str, conjuntos[1].interseccion(conjuntos[0]).elementos))
            # Mostrar los números en los círculos
            plt.text(-0.55, 0.1, numeros_conjunto1, color='blue', fontsize=10, ha='center', va='center')
            plt.text(0.3, 0.1, numeros_conjunto2, color='blue', fontsize=10, ha='center', va='center')
            plt.text(-0.13, 0.1, interseccion_12, color='blue', fontsize=10, ha='center', va='center')
            plt.title(f"Diagrama de Venn ({operacion})")
            plt.show()
        else:
            venn = venn3([conjuntos[0].elementos, conjuntos[1].elementos, conjuntos[2].elementos], set_labels=('Conjunto 1', 'Conjunto 2', 'Resultado'))
            # Obtener los números de cada conjunto
            numeros_conjunto1 = ", ".join(map(str, conjuntos[0].diferencia(conjuntos[1]).elementos))
            numeros_conjunto2 = ", ".join(map(str, conjuntos[1].diferencia(conjuntos[0]).elementos))
            # Obtener los números de la intersección
            interseccion_12 = ", ".join(map(str, conjuntos[0].interseccion(conjuntos[1]).elementos))
            # Mostrar los números en los círculos
            plt.text(-0.36, 0.1, numeros_conjunto1, color='blue', fontsize=10, ha='center', va='center')
            plt.text(0.36, 0.1, numeros_conjunto2, color='blue', fontsize=10, ha='center', va='center')
            plt.text(0, 0.1, interseccion_12, color='blue', fontsize=10, ha='center', va='center')
            plt.title(f"Diagrama de Venn ({operacion})")
            plt.show()

def main():
    # Mostrar la ventana principal
    ventana_principal = crear_ventana_principal()
    ventana_principal.mainloop()

if _name_ == "_main_":
    # Lista vacía para almacenar los conjuntos
    conjuntos = []
    main()
