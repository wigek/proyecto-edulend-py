from src.registro import registro
from src.inicioSesion import login
from src.dashboard import dashboard
from src.admin import login_admin

def menuPrincipal():
    while True:
        print("Bienvenido a Edulend \n Selecciona una de las siguientes opciones: \n 1. Registrar usuario \n 2. Inicio de sesion usuario \n 3. Inicio de sesion como administrador")
        
        opcion= input("\n Seleeciona una opción:")
        if opcion == "1":
            registro()  
        elif opcion =="2":
            user_logueado= login()
            if user_logueado:
                dashboard(user_logueado)
        elif opcion =="3":
            login_admin()
        else:
            print("\n[!] Opción no válida. Inténtalo de nuevo.")
            input("Presiona Enter para continuar")
            
if __name__ == "__main__":
    menuPrincipal()