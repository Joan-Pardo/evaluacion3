nuevo_libro = []
registro_ventas = []
cantidad = 0
def registro():
    print("-"*60)
    print("INGRESO DE DATOS DE LIBRO NUEVO: ")
    print("-"*60)
    titulo = input("INGRESE EL NOMBRE DEL LIBRO: ").lower()
    auto = input("INGRESA EL AUTOR DEL LIBRO: ").lower()
    gen = input("INGRESA EL GENERO DEL LIBRO: ").lower()
    price = int(input("PRECIO: "))
    book = [titulo , auto, gen, price]
    nuevo_libro.append(book)
   
def lista_libros():
    print("LISTADO DE TODOS LOS LIBROS: ")
    print("-"*60)
    print("TITULO\t \tAUTOR\t \t GENERO\t \tPRECIO")
    print("-"*60)
    for i in range (len(nuevo_libro)):
        print(nuevo_libro[i][0], end="\t""\t" )
        print(nuevo_libro[i][1], end="\t""\t" )
        print(nuevo_libro[i][2], end="\t""\t" )
        print(nuevo_libro[i][3], end="\t""\t" )
        print()

def ventas(nuevo_libro):
    for i in range (nuevo_libro):
        print([i], nuevo_libro)
    


while True:
    print("*"*60)
    print()
    print("¡BIENVENIDOS A LIBRERIA ALPES!")
    print()
    print("*"*60)
    print("(1)REGISTRAR LIBRO")
    print("(2)LISTA DE LIBROS")
    print("(3)REGISTRAR VENTA")
    print("(4)REPORTE DE VENTAS")
    print("(5)GENERAR TXT")
    print("(6) EXIT")
    
    op = int(input("SELECCIONA UNA OPCION: "))

    if op == 1:
        registro()
        
    elif op == 2:
        lista_libros()
    
    elif op == 3:
        ventas()
    # elif op == 4:
    #     reporte_ventas()

    # elif op == 5:
