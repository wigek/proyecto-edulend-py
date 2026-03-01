from src.registro import registro

def menuPrincipal():
    while True:
        print("Bienvenido a Edulend \n Selecciona una de las siguientes opciones: \n 1. Registrar usuario \n 2. Inicio de sesion usuario \n 3. Inicio de sesion como administrador")
        
        opcion= input("\n Seleeciona una opción:")
        if opcion == "1":
            registro()
            print("\n Registrando...")
        elif opcion =="2":
            
        elif opcion =="3":
            
        elif opcion =="4":
            
        else:
            print("\n[!] Opción no válida. Inténtalo de nuevo.")
            input("Presiona Enter para continuar...")