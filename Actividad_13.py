def ordenar(lista):
    if len(lista) <= 1:
        return lista
    pivote = lista[0]
    mayores = [x for x in lista[1:] if x.paquetes > pivote.paquetes]
    iguales = [x for x in lista if x.paquetes == pivote.paquetes]
    menores = [x for x in lista[1:] if x.paquetes < pivote.paquetes]
    return ordenar(mayores) + iguales + ordenar(menores)

class Repartidor:
    def __init__(self, nombre, paquetes, zona):
        self._nombre = nombre
        self._paquetes = paquetes
        self._zona = zona
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, value):
        if value is not None:
            self._nombre = value
        else:
            raise ValueError("Nombre no válido")
    @property
    def paquetes(self):
        return self._paquetes
    @paquetes.setter
    def paquetes(self, value):
        if value >= 0:
            self._paquetes = value
        else:
            raise ValueError("Cantidad de paquetes ingresado no válido")
    @property
    def zona(self):
        return self._zona
    @zona.setter
    def zona(self, value):
        if value is not None:
            self._zona = value
        else:
            raise ValueError("Zona ingregada no válida")
    def __str__(self):
        return f"{self.nombre} - {self.paquetes} paquetes - Zona: {self.zona}"

class EmpresaMensajeria:
    def __init__(self):
        self.repartidores = []
    def agregar_repartidor(self, repartidor):
        if repartidor.nombre in self.repartidores:
            print("Ya se ha registrado un repartidor con el nombre ingresado")
        else:
            self.repartidores.append(repartidor)
            print("El registro se completo con éxito")
    def mostrar(self):
        if not self.repartidores:
            print("No se ha registrado ningún repartidor")
        else:
            print("Repartidores registrados:")
            for x in self.repartidores:
                print(x)
            ranking = ordenar(self.repartidores)
            print("Ranking de repartidores:")
            for x in ranking:
                print(x)
    def buscar_repartidor(self, nombre):
        for repartidor in self.repartidores:
            if repartidor.nombre.lower() == nombre.lower():
                return repartidor
        return None
    def estadisticas(self):
        total_paquetes = sum([x.paquetes for x in self.repartidores])
        promedio_paquetes = total_paquetes / len(self.repartidores)
        max_paquetes = max([x.paquetes for x in self.repartidores])
        min_paquetes = min([x.paquetes for x in self.repartidores])
        mayor_repartidor = [x.nombre for x in self.repartidores if x.paquetes == max_paquetes]
        menor_repartidor = [x.nombre for x in self.repartidores if x.paquetes == min_paquetes]
        print("\nESTADÍSTICAS:")
        print(f"Total de paquetes entregados: {total_paquetes}")
        print(f"Promedio de paquetes entregados: {promedio_paquetes:.2f}")
        print(f"Repartidor(es) con más entregas: {', '.join(mayor_repartidor)}")
        print(f"Repartidor(es) con menos entregar: {', '.join(menor_repartidor)}")

empresa = EmpresaMensajeria()
opcion = "0"
while opcion != "5":
    print("==SISTEMA MENSAJERÍA==")
    print("1.Registrar repartidor")
    print("2.Mostrar repartidores registrados")
    print("3.Buscar repartidor")
    print("4.Mostrar estadísticas")
    print("5.Salir")
    opcion = input("\nSeleccione una opción: ")
    match opcion:
        case "1":
            try:
                cantidad = int(input("¿Cuántos repartidores desea registrar?: "))
                for i in range(cantidad):
                    print(f"Ingrese los datos del repartidor {i + 1}:")
                    nombre = input("\tNombre: ")
                    paquetes = int(input("\tPaquetes: "))
                    zona = input("\tZona: ")
                    repartidor = Repartidor(nombre, paquetes, zona)
                    empresa.agregar_repartidor(repartidor)
            except ValueError as e:
                print(e)
        case "2":
            empresa.mostrar()
        case "3":
            if not empresa.repartidores:
                print("No se ha registrado ninguna repartidor")
                continue
            buscar_nombre = input("Ingrese el nombre que desea consultar: ")
            resultado = empresa.buscar_repartidor(buscar_nombre)
            print(resultado)
        case "4":
            if not empresa.repartidores:
                print("Aún no hay estadisticas, registre al menos un repatidor")
                continue
            empresa.estadisticas()