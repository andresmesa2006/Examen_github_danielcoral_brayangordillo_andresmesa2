from registro_usu import registrar_usuarios
from regsitro_est import registro_estudiante
def mostrar_menu():
    print("\nBienvenido al gestor de notas:")
    print("--MENU--")
    print("1. Registrar usuario")
    print("2. Registrar estudiante")
def main():
    while True:
            mostrar_menu()
            opcion = input("Elija una opción: ")
            if opcion == "1":
                registrar_usuarios()
            elif opcion == "2":
                registro_estudiante()
                break
if __name__ == "__main__":
    main()
