# Lista con datos de vehículos y sus servicios en el taller
# Cada vehículo tiene: [patente, marca, modelo, año, dueño, servicio, precio]
lista_vehiculos = [
    ["AA123BB", "Ford", "Fiesta", 2015, "Juan Pérez", "Cambio de aceite", 4500],
    ["AB456CD", "Chevrolet", "Onix", 2018, "María Gómez", "Frenos", 8500],
    ["AC789EF", "Toyota", "Corolla", 2020, "Carlos Díaz", "Revisión general", 12000],
    ["AD321GH", "Renault", "Kangoo", 2012, "Sofía Rivas", "Cambio de embrague", 23000],
    ["AE654IJ", "Volkswagen", "Gol", 2017, "Pedro Luna", "Alineación y balanceo", 7500],
    ["AF987KL", "Peugeot", "208", 2019, "Lucía Romero", "Cambio de batería", 9500],
    ["AG111MN", "Honda", "Civic", 2021, "Federico Torres", "Revisión general", 13000],
    ["AH222OP", "Fiat", "Cronos", 2022, "Mariana Díaz", "Cambio de aceite", 4800],
    ["AI333QR", "Nissan", "March", 2016, "Ricardo López", "Frenos", 8200],
    ["AJ444ST", "Citroën", "C3", 2018, "Laura Suárez", "Suspensión", 11000]
]

class Vehiculo():
    """
    Clase que representa un vehículo en el taller mecánico
    Contiene todos los datos del vehículo y su servicio
    """
    def __init__(self, patente, marca, modelo, año, dueño, servicio, precio):
        # Inicializa todos los atributos del vehículo
        self.patente = patente      # Número de patente del vehículo
        self.marca = marca          # Marca del vehículo (ej: Ford, Toyota)
        self.modelo = modelo        # Modelo del vehículo (ej: Fiesta, Corolla)
        self.año = año              # Año de fabricación
        self.dueño = dueño          # Nombre del dueño/propietario
        self.servicio = servicio    # Tipo de servicio/reparación requerida
        self.precio = precio        # Costo del servicio

    def mostrar_todos_los_datos(self):
        """
        Muestra todos los datos del vehículo en formato legible
        """
        print(f"""Patente:{self.patente}
Marca:{self.marca}
Modelo:{self.modelo}
Año:{self.año}
Dueño:{self.dueño}
Servicio:{self.servicio}
Precio:{self.precio}""")
        print("-"*100)  # Línea separadora para mejor visualización
    

class ConsultasVehiculo():
    """
    Clase para realizar consultas y operaciones sobre la lista de vehículos
    """
    def __init__(self, lista_vehiculos):
        # Convierte la lista de datos en objetos Vehiculo
        self.vehiculos = [Vehiculo(*datos) for datos in lista_vehiculos]

    def mostrar_datos_por_patente(self, pedir_patente):
        """
        Busca y muestra los datos de un vehículo por su patente
        """
        for vehiculo in self.vehiculos:
            # Compara patentes sin importar mayúsculas/minúsculas
            if vehiculo.patente.lower() == pedir_patente.lower():
                vehiculo.mostrar_todos_los_datos()
    
    def mostrar_reparacion_especifica(self, pedir_reparacion):
        """
        Muestra todos los vehículos que requieren un tipo específico de reparación
        """
        for vehiculo in self.vehiculos:
            if vehiculo.servicio.lower() == pedir_reparacion.lower():
                vehiculo.mostrar_todos_los_datos()
    
    def vehiculos_mas_nuevos(self, año_pedido):
        """
        Muestra los vehículos con año igual o mayor al especificado
        """
        for vehiculo in self.vehiculos:
            if vehiculo.año >= año_pedido:
                vehiculo.mostrar_todos_los_datos()
    
    def solo_dueño_reparacion(self):
        """
        Muestra solo el dueño y la reparación de todos los vehículos
        (vista simplificada)
        """
        for vehiculo in self.vehiculos:
            print(f"""Dueño:{vehiculo.dueño}
Reparacion:{vehiculo.servicio}""")
            print("-"*100)
    
    def modificar_dato(self, patente):
        """
        Permite modificar los datos de un vehículo específico
        """
        for v in self.vehiculos:
            if v.patente.lower() == patente.lower():
                print("Vehículo encontrado:")
                v.mostrar_todos_los_datos()
                
                # Menú de opciones para modificar
                print("""1. Marca
2. Modelo
3. Año
4. Dueño
5. Servicio
6. Precio""")
                
                opcion = int(input("Opción: "))
                
                # Modifica el campo seleccionado según la opción
                if opcion == 1:
                    v.marca = input("Nueva marca: ")
                elif opcion == 2:
                    v.modelo = input("Nuevo modelo: ")
                elif opcion == 3:
                    v.año = int(input("Nuevo año: "))
                elif opcion == 4:
                    v.dueño = input("Nuevo dueño: ")  # Corregido: era int(input()) pero dueño es string
                elif opcion == 5:
                    v.servicio = input("Nuevo servicio: ")
                elif opcion == 6:
                    v.precio = float(input("Nuevo precio: "))

        print("Datos modificados")
        v.mostrar_todos_los_datos()

            
# PROGRAMA PRINCIPAL - MENÚ INTERACTIVO
while True:
    print("MENÚ DE OPCIONES")
    print("""1-Ver todos los vehiculos ingresados
2-Mostrar datos de vehiculo por patente
3-Mostrar los vehiculos que requieren una reparación especifica
4-Vehiculos más nuevos
5-Solo dueño y reparación
6-Modificar dato
7-Salir""")
    
    a = int(input("Elección: "))
    
    # Opción 1: Mostrar todos los vehículos
    if a == 1:
        for patente, marca, modelo, año, dueño, servicio, precio in lista_vehiculos:
            vehiculo = Vehiculo(patente, marca, modelo, año, dueño, servicio, precio)
            vehiculo.mostrar_todos_los_datos()

    # Opción 2: Buscar vehículo por patente
    elif a == 2:
        pedir_patente = input("¿Cuál es la patente?: ")
        analisis = ConsultasVehiculo(lista_vehiculos)
        analisis.mostrar_datos_por_patente(pedir_patente)

    # Opción 3: Filtrar por tipo de reparación
    elif a == 3:
        pedir_reparacion = input("¿Cuál es la reparación?: ")
        analisis = ConsultasVehiculo(lista_vehiculos)
        analisis.mostrar_reparacion_especifica(pedir_reparacion)
    
    # Opción 4: Mostrar vehículos desde cierto año
    elif a == 4:
        año_pedido = int(input("Ingrese el año: "))
        analisis = ConsultasVehiculo(lista_vehiculos)
        analisis.vehiculos_mas_nuevos(año_pedido)

    # Opción 5: Mostrar resumen dueño-reparación
    elif a == 5:
        analisis = ConsultasVehiculo(lista_vehiculos)
        analisis.solo_dueño_reparacion()

    # Opción 6: Modificar datos de un vehículo
    elif a == 6:
        pedir_patente = input("Patente del vehículo: ")
        analisis = ConsultasVehiculo(lista_vehiculos)
        analisis.modificar_dato(pedir_patente)
    
    # Opción 7: Salir del programa
    elif a == 7: 
        break

# Mensaje de despedida
print("Gracias por usar")