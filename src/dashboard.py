import os
from src.database import loans

def dashboard(user_current):
    
    while True:
        opcion= input(f"Bienvenido al panel principal {user_current['name']}\n Ingresa una de las siguientes opciones: \n 1. Soliciar prestamo de articulo \n 2. Estado de prestamos \n 3. Datos de usuario \n 4. ¿Quienes somos? \n 5. Cerrar sesión")
        if opcion == "1":
            print("\n----------------------")
            article= input("Que artículo necesitas? (Portatil, Libro o tablet)")
            days= input("Por cuantos días?")
            new_loan={
                "user": user_current['email'],
                "article": article,
                "days": days
            }
            loans.append(new_loan)
            print(f"\n La solicidutd del prestamo de '{article}' ha sido registrada con éxito")
            input("Presiona enter para continuar")
        elif opcion == "2":
            print(f"\n El estado de prestamo de {user_current['name']}")
            found= False
            for i in loans:
                if i['user']== user_current['email']:
                    print(f"\n Articulo: {i['article']} - Días: {i['days']}")
                    found= True
            if not found:
                print("No tienes préstamos registrados") 
            input("\n Presiona enter para salir")
        elif opcion == "3":
            print(f"\nNombre:{user_current['name']}")
            print(f"\nCorreo electronico:{user_current['email']}")
            print("\n Presiona Enter para volver")
        elif opcion == "4":
            print("\nEdulend")
        elif opcion == "5":
            print("\nCerrando sesión...")
            break 
        else:
            print("\nIngresa una opción válida")