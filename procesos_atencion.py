

class Proceso:

    def view(self):
        
        self.name_process = input("Que desea realizar: ")
        self.cantidad_process = input("Introduce la cantidad: ")

        return print(f"el proceso de {self.name_process} inicio y la cantida es {self.cantidad_process}")

class Fotocopias(Proceso):

    def __init__(self):
        super().__init__()

class ImpresionColor(Proceso):

    def __init__(self) -> None:
        super().__init__()

class ImpresionBN(Proceso):

    def __init__(self) -> None:
        super().__init__()

class Scanner(Proceso):

    def __init__(self) -> None:
        super().__init__()


proceso1 = Fotocopias()


while True:

    print("Fotocopias Fran..\n")
    print("1. Sacar fotocopia: ")
    print("2. Sacar impresion a color: ")
    print("3. Sacar impresion B/N")
    print("4. Hacer scanner: ")
    print("5. salis ")

    option = input("Que desea realizar?, ELija una opción: ")

    match option:

        case "1":
            proceso1.view()  
        case "2":
            proceso1.view()
        case "3":
            proceso1.view()            
        case "4":
            proceso1.view()
        case "5":
            print("Saliendo del programa...")
            break
        case _:
            print("Has introduccido una opción invaliad. Por favor ingrese otra opciòn: ")