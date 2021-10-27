from collections import namedtuple
import os
import csv
Consolas = namedtuple("Consolas", "Folio, Fecha_venta, Descripcion, Cantidad, Precio")
lista_Consolas = []

while True:
    print("")
    print("******** VENTA DE CONSOLAS ******")
    print("")
    print("Buenos dias, usted esta entrando al registro de  venta de consolas")
    print("****  Por favor indique la opcion que ocupe***")
    print("Registrar una venta [1]")
    print("Consulta de una venta [2]")
    print("Convertir a csv [3]")
    print("Salir del Menu [4]")
    op = input('Que opcion desea escoger:')
    print("")
    
    if op == '1':
        Folio = (int(input("Introduce el folio: ")))
        Fecha_venta = (input("Introduce la fecha de la venta que se realizo: "))
        Descripcion = (input("Por favor describe de la consola que se vendio: "))
        Cantidad = (int(input("Cuantas consolas fueron que se  vendieron: ")))
        Precio = (int(input("Cual fue el precio por consola: ")))
        subtotal = Cantidad * Precio
        print(f"El subtotal a pagar es {subtotal}")
        IVA = (subtotal*0.16)
        Total = (subtotal + IVA)
        print(f"El monto final con IVA incluido es de {Total}")
        ventas = Consolas(Folio, Fecha_venta, Descripcion, Cantidad, Precio)
        lista_Consolas.append(ventas)
    elif op == '2':
        Folio_busqueda = (int(input("Introduce el folio que quieres buscar: ")))
        for elemento in lista_Consolas:
            if elemento.Folio == Folio_busqueda:
                print(f"Fecha de venta: {elemento.Fecha_venta}")
                print(f"Descripcion: {elemento.Descripcion}")
                print(f"Cantidad: {elemento.Cantidad}")
                print(f"Precio: {elemento.Precio}")
                break
        else:
            print("No existe ese  folio")
            print("por favor ingrese el folio correcto")
    elif op == '3':
        input("desea guardar sus registros en un csv?:")
        with open("Evidencia_estructura2.csv","w",newline="") as archivo:
         grabador = csv.writer(archivo)
         grabador.writerow(("Consolas", "Folio, Fecha_venta, Descripcion, Cantidad, Precio"))
         grabador.writerows([(Consolas, elemento.Folio, elemento.Fecha_venta, elemento.Descripcion, elemento.Cantidad, elemento.Precio) for elemento in lista_Consolas])
        print(f"se guardo exitosamente en {os.getcwd()}")
        
    elif op == '4' :
        print('Usted ha salido del menu')
        break